import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify

from core.markdown_utils import clean_markdown
from core.models import InterviewQuestion, PracticeQuestion, Question, Topic


TOPICS = {
    '1': ('Basics', 'basics'),
    '2': ('Control Flow', 'control-flow'),
    '3': ('Functions', 'functions'),
    '4': ('Strings', 'strings'),
    '5': ('Data Structures (List, Tuple, Dict, Set)', 'data-structures'),
    '6': ('Object-Oriented Programming (OOP)', 'object-oriented-programming'),
    '7': ('Exception Handling', 'exception-handling'),
    '8': ('File Handling', 'file-handling'),
    '9': ('Iterators & Generators', 'iterators-and-generators'),
    '10': ('Functional Programming (map/filter/reduce/decorators)', 'functional-programming'),
    '11': ('Modules & Packages', 'modules-and-packages'),
    '12': ('Advanced Python (Memory, GIL, Threading, Async, Metaclasses)', 'advanced-python'),
    '13': ('Python Internals & Ecosystem', 'python-internals-and-ecosystem'),
    '14': ('Testing & Best Practices', 'testing-and-best-practices'),
    '15': ('Quick Revision — All Concepts, Simple Definitions', 'quick-revision'),
    '16': ('Important Interview Questions (Final Round Prep)', 'important-interview-questions'),
}


def numbered_items(text):
    return [
        match.group(1).strip()
        for match in re.finditer(r'^\s*\d+\.\s+(.+?)\s*$', text, re.MULTILINE)
    ]


def extract_code(text):
    match = re.search(r'```(?:python)?\s*\n(.*?)```', text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ''


class Command(BaseCommand):
    help = 'Import the complete Python interview guide from README.md or another Markdown file.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=Path, nargs='?', default=Path('README.md'), help='Path to the Python interview guide Markdown file.')

    @transaction.atomic
    def handle(self, *args, **options):
        path = options['path']
        if not path.is_file():
            raise CommandError(f'Guide file not found: {path}')

        source = path.read_text(encoding='utf-8')
        sections = list(re.finditer(r'^#\s+(\d+)\.\s+(.+?)\s*$', source, re.MULTILINE))
        imported = 0

        for position, section in enumerate(sections):
            if section.group(1) == 'INDEX':
                continue
            end = sections[position + 1].start() if position + 1 < len(sections) else len(source)
            content = source[section.start():end].strip()
            name, slug = TOPICS.get(section.group(1), (section.group(2).strip().title(), slugify(section.group(2))))
            topic, _ = Topic.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'definition': self._definition(content),
                    'guide_content': content,
                    'display_order': int(section.group(1)),
                },
            )
            topic.questions.all().delete()
            topic.practice_questions.all().delete()
            topic.interview_questions.all().delete()

            practice_marker = re.search(r'^###\s+.*Practice Questions.*$', content, re.MULTILINE | re.IGNORECASE)
            question_source = content[:practice_marker.start()] if practice_marker else content
            question_blocks = list(re.finditer(r'^###\s+(?!.*Practice Questions)(.+?)\s*$', question_source, re.MULTILINE | re.IGNORECASE))
            questions = []
            for index, heading in enumerate(question_blocks):
                body_end = question_blocks[index + 1].start() if index + 1 < len(question_blocks) else len(question_source)
                body = question_source[heading.end():body_end].strip()
                questions.append(Question(
                    topic=topic,
                    question_text=heading.group(1).strip(),
                    answer_text=clean_markdown(re.sub(r'```(?:python)?\s*\n.*?```', '', body, flags=re.DOTALL | re.IGNORECASE)),
                    code_example=extract_code(body),
                ))
            Question.objects.bulk_create(questions)

            if practice_marker:
                practice_end = re.search(r'^#\s+\d+\.\s+', content[practice_marker.end():], re.MULTILINE)
                practice_text = content[practice_marker.end():practice_marker.end() + practice_end.start()] if practice_end else content[practice_marker.end():]
                PracticeQuestion.objects.bulk_create([
                    PracticeQuestion(topic=topic, question_text=item, hint_text='Review the related concepts and work through an example.')
                    for item in numbered_items(practice_text)
                ])

            if section.group(1) == '16':
                InterviewQuestion.objects.bulk_create([
                    InterviewQuestion(topic=topic, question_text=item)
                    for item in numbered_items(content)
                ])
            imported += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {imported} guide sections from {path}.'))

    @staticmethod
    def _definition(content):
        match = re.search(r'\*\*Simple definition:\*\*\s*(.+)', content)
        return clean_markdown(match.group(1)) if match else 'Complete Python interview preparation guide.'
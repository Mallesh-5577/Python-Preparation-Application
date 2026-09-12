import re

from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count

from .models import Topic
from .markdown_utils import clean_markdown


def home_view(request):
	return render(request, 'home.html', {'topic_count': Topic.objects.count()})


def topics_view(request):
	query = request.GET.get('q', '').strip()
	topics = Topic.objects.annotate(
		questions_count=Count('questions', distinct=True),
		practice_count=Count('practice_questions', distinct=True),
	).order_by('display_order', 'name')
	if query:
		topics = topics.filter(name__icontains=query)
	return render(request, 'topics.html', {'topics': topics, 'query': query})


def topic_detail_view(request, slug):
	topic = get_object_or_404(Topic, slug=slug)
	questions = topic.questions.all()
	return render(request, 'topic_detail.html', {
		'topic': topic,
		'questions': questions,
		'guide_sections': parse_guide_sections(topic.guide_content),
	})


def parse_guide_sections(content):
	if not content:
		return []

	sections = []
	current = None
	in_code = False
	code_lines = []
	text_lines = []

	def flush_text():
		if current is not None and text_lines:
			text = clean_markdown('\n'.join(text_lines))
			if text:
				current['paragraphs'].append(text)
			text_lines.clear()

	def flush_code():
		if current is not None and code_lines:
			current['code_blocks'].append('\n'.join(code_lines).strip())
			code_lines.clear()

	for line in content.splitlines():
		if line.startswith('```'):
			if in_code:
				flush_code()
			else:
				flush_text()
			in_code = not in_code
			continue
		if in_code:
			code_lines.append(line)
			continue
		match = re.match(r'^#{2,3}\s+(.+?)\s*$', line)
		if match:
			flush_text()
			if 'practice questions' in match.group(1).lower():
				break
			heading = clean_markdown(match.group(1))
			if heading.casefold() == 'overview':
				current = None
				continue
			current = {'heading': heading, 'paragraphs': [], 'code_blocks': []}
			sections.append(current)
			continue
		if line.startswith('# '):
			continue
		if current is None:
			continue
		text_lines.append(line)

	flush_text()
	flush_code()
	return sections


def practice_questions_view(request):
	topics = Topic.objects.prefetch_related('practice_questions').all()
	return render(request, 'practice_questions.html', {'topics': topics})


def interview_questions_view(request):
	topics = Topic.objects.prefetch_related('interview_questions').all()
	return render(request, 'interview_questions.html', {'topics': topics})

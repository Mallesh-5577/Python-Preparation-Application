from django.db import models


class Topic(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	definition = models.TextField()
	display_order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['display_order', 'name']

	def __str__(self):
		return self.name


class Question(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
	question_text = models.TextField()
	answer_text = models.TextField()
	code_example = models.TextField(blank=True)

	def __str__(self):
		return self.question_text[:80]


class PracticeQuestion(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='practice_questions')
	question_text = models.TextField()
	hint_text = models.TextField()

	def __str__(self):
		return self.question_text[:80]


class InterviewQuestion(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='interview_questions')
	question_text = models.TextField()

	def __str__(self):
		return self.question_text[:80]

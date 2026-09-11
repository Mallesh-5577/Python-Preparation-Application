from django.shortcuts import get_object_or_404, redirect, render

from .models import Topic


def home_view(request):
	return render(request, 'home.html', {'topic_count': Topic.objects.count()})


def topics_view(request):
	query = request.GET.get('q', '').strip()
	topics = Topic.objects.all()
	if query:
		topics = topics.filter(name__icontains=query)
	return render(request, 'topics.html', {'topics': topics, 'query': query})


def topic_detail_view(request, slug):
	topic = get_object_or_404(Topic, slug=slug)
	questions = topic.questions.all()
	return render(request, 'topic_detail.html', {'topic': topic, 'questions': questions})


def practice_questions_view(request):
	topics = Topic.objects.prefetch_related('practice_questions').all()
	return render(request, 'practice_questions.html', {'topics': topics})


def interview_questions_view(request):
	topics = Topic.objects.prefetch_related('interview_questions').all()
	return render(request, 'interview_questions.html', {'topics': topics})

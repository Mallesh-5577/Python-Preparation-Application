from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, SignupForm
from .models import Topic


def home_view(request):
	return render(request, 'home.html', {'topic_count': Topic.objects.count()})


def signup_view(request):
	if request.user.is_authenticated:
		return redirect('core:home')
	form = SignupForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		user = form.save()
		login(request, user)
		messages.success(request, 'Your account is ready. Welcome to the preparation room.')
		return redirect('core:home')
	return render(request, 'signup.html', {'form': form})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('core:home')
	form = LoginForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		user = authenticate(
			request,
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password'],
		)
		if user is not None:
			login(request, user)
			messages.success(request, 'Welcome back. Let us keep learning.')
			return redirect('core:home')
		form.add_error(None, 'That username and password combination was not found.')
	return render(request, 'login.html', {'form': form})


def logout_view(request):
	logout(request)
	messages.info(request, 'You have been logged out.')
	return redirect('core:home')


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

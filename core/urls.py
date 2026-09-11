from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('topics/', views.topics_view, name='topics'),
    path('topics/<slug:slug>/', views.topic_detail_view, name='topic-detail'),
    path('practice-questions/', views.practice_questions_view, name='practice-questions'),
    path('interview-questions/', views.interview_questions_view, name='interview-questions'),
]
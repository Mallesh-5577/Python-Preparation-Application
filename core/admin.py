from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import InterviewQuestion, PracticeQuestion, Question, Topic


admin.site.unregister(User)


@admin.register(User)
class SiteUserAdmin(UserAdmin):
	list_display = (
		'username', 'email', 'first_name', 'last_name',
		'is_active', 'is_staff', 'date_joined', 'last_login',
	)
	list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined')
	search_fields = ('username', 'email', 'first_name', 'last_name')
	ordering = ('-date_joined',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	search_fields = ('name', 'definition')
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'topic')
	list_filter = ('topic',)
	search_fields = ('question_text', 'answer_text')


@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'topic')
	list_filter = ('topic',)
	search_fields = ('question_text', 'hint_text')


@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'topic')
	list_filter = ('topic',)
	search_fields = ('question_text',)

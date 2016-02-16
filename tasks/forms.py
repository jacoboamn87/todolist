from django import forms

from extra_views import InlineFormSet

from tasks.models import Task, List


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['author', 'created_at', 'updated_at']


class TasksInline(InlineFormSet):
    model = Task


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ['author', 'created_at', 'updated_at']

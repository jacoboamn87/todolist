from django import forms

from tasks.models import Task, List


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['author', 'created_at', 'updated_at']


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ['author', 'created_at', 'updated_at']

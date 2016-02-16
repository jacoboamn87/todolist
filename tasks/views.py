from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from extra_views import (
    CreateWithInlinesView, UpdateWithInlinesView
)

from tasks.models import Task, List
from tasks.forms import TaskForm, TasksInline, ListForm


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super(generic.CreateView, self).form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class ListDetailView(generic.DetailView):
    model = List
    template_name = 'tasks/list_detail.html'
    context_object_name = 'todolist'

    def get_queryset(self):
        return List.objects.filter(author=self.request.user)


class ListWithTasksCreateView(CreateWithInlinesView):
    model = List
    form_class = ListForm
    inlines = [TasksInline]
    template_name = 'tasks/list_form_with_inlines.html'

    def get_success_url(self):
        return reverse_lazy('tasks:list_list')

    def forms_valid(self, form, inlines):
        """
        If the form and formsets are valid, save the associated models.
        """
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        for formset in inlines:
            formset.save()
        return HttpResponseRedirect(self.get_success_url())


class ListWithTasksUpdateView(UpdateWithInlinesView):
    model = List
    form_class = ListForm
    inlines = [TasksInline]
    template_name = 'tasks/list_form_with_inlines.html'

    def get_success_url(self):
        return reverse_lazy('tasks:list_list')


class ListListView(generic.ListView):
    model = List
    template_name = 'tasks/list_list.html'
    context_object_name = 'lists'

    def get_queryset(self):
        return List.objects.filter(author=self.request.user)


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'tasks/list_form.html'
    form_class = ListForm
    success_url = reverse_lazy('tasks:list_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super(generic.CreateView, self).form_valid(form)


class ListUpdateView(generic.UpdateView):
    model = List
    template_name = 'tasks/list_form.html'
    form_class = ListForm
    success_url = reverse_lazy('tasks:list_list')

    def get_queryset(self):
        return List.objects.filter(author=self.request.user)

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from tasks.models import Task, List
from tasks.forms import TaskForm, ListForm


def task_detail(request, *args, **kwargs):
    task = get_object_or_404(Task, author=request.user, pk=kwargs['pk'])
    ctx = {'task': task}
    return render(request, 'tasks/task_detail.html', ctx)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()

            return HttpResponseRedirect(reverse('tasks_traditional:task_list'))
        else:
            ctx = {'form': form}
    else:
        ctx = {'form': TaskForm()}

    return render(request, 'tasks/task_form.html', ctx)


def task_list(request):
    tasks = Task.objects.filter(author=request.user)
    ctx = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', ctx)


def list_list(request):
    lists = List.objects.filter(author=request.user)
    ctx = {'lists': lists}
    return render(request, 'tasks/list_list.html', ctx)

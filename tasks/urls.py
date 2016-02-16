from django.conf.urls import url

from tasks.views import (
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView,
    ListDetailView, ListListView, ListCreateView, ListUpdateView,
    ListWithTasksCreateView, ListWithTasksUpdateView
)

app_name = 'tasks'

urlpatterns = [
    url(r'^$', TaskListView.as_view(), name='task_list'),
    url(r'^(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task_detail'),
    url(r'^create/$', TaskCreateView.as_view(), name='task_create'),
    url(r'^(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='task_edit'),

    url(r'^list/(?P<pk>\d+)/$', ListDetailView.as_view(), name='list_detail'),
    url(r'^list/create/$', ListCreateView.as_view(), name='list_create'),
    url(
        r'^list/(?P<pk>\d+)/edit/$', ListUpdateView.as_view(),
        name='list_edit'
    ),
    url(r'^lists/$', ListListView.as_view(), name='list_list'),
    url(
        r'^list/with-tasks/$', ListWithTasksCreateView.as_view(),
        name='list_tasks_create'
    ),
    url(
        r'^list/with-tasks/(?P<pk>\d+)/edit/$',
        ListWithTasksUpdateView.as_view(),
        name='list_tasks_edit'
    ),
]

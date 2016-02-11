from django.conf.urls import url

from tasks.views import (
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView,
    ListDetailView
)

app_name = 'tasks'

urlpatterns = [
    url(r'^$', TaskListView.as_view(), name='task_list'),
    url(r'^(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task_detail'),
    url(r'^create/$', TaskCreateView.as_view(), name='task_create'),
    url(r'^(?P<pk>\d+)/edit/$', TaskUpdateView.as_view(), name='task_edit'),

    url(r'^list/(?P<pk>\d+)/$', ListDetailView.as_view(), name='list_detail'),
]

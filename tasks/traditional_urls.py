from django.conf.urls import url

from tasks import traditional_views

app_name = 'tasks_traditional'

urlpatterns = [
    url(r'^$', traditional_views.task_list, name='task_list'),
    url(r'^(?P<pk>\d+)/$', traditional_views.task_detail, name='task_detail'),
]

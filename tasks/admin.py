from django.contrib import admin

from tasks.models import Task, List

admin.site.register(Task)
admin.site.register(List)

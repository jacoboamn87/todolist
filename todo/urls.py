from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^tasks/', include('tasks.urls')),

    # Django Admin
    url(r'^admin/', admin.site.urls),
]

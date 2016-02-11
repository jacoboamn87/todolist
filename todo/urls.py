from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^tasks/', include('tasks.urls')),
    url(r'^tasks-traditional/', include('tasks.traditional_urls')),

    # Django Authentication
    url(r'^account/', include('django.contrib.auth.urls')),

    # Django Admin
    url(r'^admin/', admin.site.urls),
]

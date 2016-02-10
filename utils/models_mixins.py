from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Signable(object):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)


class Timestampable(object):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

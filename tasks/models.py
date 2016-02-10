from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from utils.models_mixins import (
    Signable, Timestampable
)


class Task(models.Model, Signable, Timestampable):
    name = models.CharField(_('Name'), null=False, blank=False, max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    due_date = models.DateTimeField(_('Due Date'), null=True, blank=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Define custom methods here


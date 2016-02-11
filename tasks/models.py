from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from utils.models_mixins import (
    Signable, Timestampable
)


@python_2_unicode_compatible
class List(models.Model, Signable, Timestampable):
    name = models.CharField(_('Name'), null=False, blank=False, max_length=255)

    class Meta:
        verbose_name = _('List')
        verbose_name_plural = _('Lists')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('')


@python_2_unicode_compatible
class Task(models.Model, Signable, Timestampable):
    LOWEST = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    HIGHEST = 5

    PRIORITY_CHOICES = [
        (LOWEST, _('Lowest')),
        (LOW, _('Low')),
        (MEDIUM, _('Medium')),
        (HIGH, _('High')),
        (HIGHEST, _('Highest')),
    ]

    name = models.CharField(_('Name'), null=False, blank=False, max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    due_date = models.DateTimeField(_('Due Date'), null=True, blank=True)
    priority = models.IntegerField(
        _('Priority'), choices=PRIORITY_CHOICES,
        null=False, blank=False, default=LOWEST
    )
    todo_list = models.ForeignKey(
        List, verbose_name=_('List'), null=True, blank=True
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('')

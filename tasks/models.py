from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


class List(models.Model):
    name = models.CharField(_('Name'), null=False, blank=False, max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('List')
        verbose_name_plural = _('Lists')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('')


class Task(models.Model):
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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('')

    def get_priority(self):
        for pair in self.PRIORITY_CHOICES:
            if self.priority == pair[0]:
                return pair[1]

        return self.priority

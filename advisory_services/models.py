from django.db import models
from advisory_commons.models import AdvisoryBaseModel, Tag
from advisory_team.models import TeamMember
from advisory_events.models import Events
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from downcode import downcode


# Create your models here.
class Department(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    slug = models.SlugField(max_length=255, verbose_name=_('slug'))
    team_members = models.ManyToManyField(TeamMember, related_name='departments', verbose_name=_('team members'), null=True, blank=True)
    events = models.ManyToManyField(Events, related_name='departments', verbose_name=_('events'), null=True, blank=True)

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


class Service(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    slug = models.SlugField(max_length=255, verbose_name=_('slug'))
    department = models.ForeignKey(Department, related_name='services', on_delete=models.CASCADE, verbose_name=_('department'))
    team_members = models.ManyToManyField(TeamMember, related_name='services', verbose_name=_('team members'), null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='services', verbose_name=_('tags'), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

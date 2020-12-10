from django.db import models
from advisory_commons.models import AdvisoryBaseModel, Tag
from advisory_team.models import TeamMember
from django.utils.translation import gettext_lazy as __
from django.utils.text import slugify
from downcode import downcode

# Create your models here.
class Department(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=__('name'))
    slug = models.SlugField(max_length=255, verbose_name=__('slug'))
    team_members = models.ManyToManyField(TeamMember, related_name=__('departments'), verbose_name=__('team members'), null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = __('Department')
        verbose_name_plural = __('Departments')


class Service(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=__('name'))
    slug = models.SlugField(max_length=255, verbose_name=__('slug'))
    department = models.ForeignKey(Department, related_name=__('services'), on_delete=models.CASCADE, verbose_name=__('department'))
    team_members = models.ManyToManyField(TeamMember, related_name=__('services'), verbose_name=__('team members'), null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name=__('services'), verbose_name=__('tags'), null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = __('Service')
        verbose_name_plural = __('Services')

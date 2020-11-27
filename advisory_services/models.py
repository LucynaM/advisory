from django.db import models
from advisory_commons.models import AdvisoryBaseModel, Tag
from advisory_team.models import TeamMember
from django.utils.translation import gettext_lazy as __


# Create your models here.
class Department(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=__('name'))
    team_members = models.ManyToManyField(TeamMember, related_name=__('departments'), verbose_name=__('team members'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __('Department')
        verbose_name_plural = __('Departments')


class Service(AdvisoryBaseModel):
    name = models.CharField(max_length=255, verbose_name=__('name'))
    department = models.ForeignKey(Department, related_name=__('services'), on_delete=models.CASCADE, verbose_name=__('department'))
    team_members = models.ManyToManyField(TeamMember, related_name=__('services'), verbose_name=__('team members'))
    tags = models.ManyToManyField(Tag, related_name=__('services'), verbose_name=__('tags'))

    class Meta:
        verbose_name = __('Service')
        verbose_name_plural = __('Services')

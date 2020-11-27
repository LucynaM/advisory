from django.db import models
from advisory_commons.models import AdvisoryBaseModel
from django.utils.translation import gettext_lazy as __


# Create your models here.
class Specialization(models.Model):
    specialization = models.CharField(max_length=255, verbose_name = __('specialization'))

    @property
    def name(self):
        return self.specialization

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __('Specialization')
        verbose_name_plural = __('Specializations')


class TeamMember(AdvisoryBaseModel):
    first_name = models.CharField(max_length=64, verbose_name=__('first_name'))
    last_name = models.CharField(max_length=64, verbose_name=__('last_name'))
    academic_title = models.CharField(max_length=32, verbose_name=__('academic_title'), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=__('title'))
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, verbose_name=__('phone'))
    specializations = models.ManyToManyField(Specialization, related_name=__('team_members'), verbose_name=__('specializations'))

    REQUIRED_FIELDS = ['email', 'phone']

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __('Team Member')
        verbose_name_plural = __('Team Members')

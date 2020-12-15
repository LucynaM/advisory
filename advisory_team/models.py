from django.db import models
from advisory_commons.models import AdvisoryBaseModel
from django.utils.translation import gettext_lazy as __
from django.utils.text import slugify
from downcode import downcode


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
    slug = models.SlugField(max_length=255, verbose_name=__('slug'))
    academic_title = models.CharField(max_length=32, verbose_name=__('academic_title'), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=__('title'))
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, verbose_name=__('phone'))
    specializations = models.ManyToManyField(Specialization, related_name=__('team_members'), verbose_name=__('specializations'), null=True, blank=True)
    html_id = models.CharField(max_length=128, verbose_name=__('html_id'), null=True, blank=True)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode('{} {}'.format(self.name, self.title)))
        self.html_id = '{}{}'.format(downcode(self.first_name), downcode(self.last_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = __('Team Member')
        verbose_name_plural = __('Team Members')

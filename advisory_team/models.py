from django.db import models
from advisory_commons.models import AdvisoryBaseModel
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from downcode import downcode
import re
from django.core.exceptions import ValidationError


# Create your models here.
class Specialization(models.Model):
    specialization = models.CharField(max_length=255, verbose_name = _('specialization'))

    @property
    def name(self):
        return self.specialization

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = _('Specialization')
        verbose_name_plural = _('Specializations')


def only_int(value):
    if not value.isdigit():
        raise ValidationError(_('Pole powinno zawierać wyłącznie cyfry'))


class TeamMember(AdvisoryBaseModel):
    first_name = models.CharField(max_length=64, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=64, verbose_name=_('last_name'))
    slug = models.SlugField(max_length=255, verbose_name=_('slug'))
    academic_title = models.CharField(max_length=32, verbose_name=_('academic_title'), null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name=_('title'))
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32, unique=True, verbose_name=_('phone'), validators=[only_int])
    specializations = models.ManyToManyField(Specialization, related_name='team_members', verbose_name=_('specializations'), null=True, blank=True)
    html_id = models.CharField(max_length=128, verbose_name=_('html_id'), null=True, blank=True)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def change_phone(self):
        new_phone = str(self.phone)[::-1]
        splited = re.findall('.{1,3}', new_phone)
        joined = ' '.join(splited)[::-1]
        return joined


    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode('{} {}'.format(self.name, self.title)))
        self.html_id = '{}{}'.format(downcode(self.first_name), downcode(self.last_name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')

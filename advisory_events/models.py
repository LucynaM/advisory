from django.db import models
from advisory_commons.models import AdvisoryBaseModel, Tag
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from downcode import downcode

# Create your models here.


class Events(AdvisoryBaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, verbose_name=_('slug'))
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('creation_date'))
    tags = models.ManyToManyField(Tag, related_name='events', verbose_name=_('tags'), null=True, blank=True)

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(downcode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Events')
        verbose_name_plural = _('Events')

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=255, verbose_name=_('tag'))

    @property
    def name(self):
        return self.tag

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class AdvisoryBaseModel(models.Model):
    content = models.TextField(verbose_name=_('content'))
    photo_desktop = models.ImageField(upload_to='images/desktop', null=True, blank=True, verbose_name=_('photo desktop'))
    photo_mobile = models.ImageField(upload_to='images/mobile', null=True, blank=True, verbose_name=_('photo mobile'))

    class Meta:
        abstract = True

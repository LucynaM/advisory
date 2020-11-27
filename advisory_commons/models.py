from django.db import models
from django.utils.translation import gettext_lazy as __


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=255, verbose_name=__('tag'))

    @property
    def name(self):
        return self.tag

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __('Tag')
        verbose_name_plural = __('Tags')


class AdvisoryBaseModel(models.Model):
    content = models.TextField(verbose_name=__('content'))
    photo_desktop = models.ImageField(upload_to='images/desktop', null=True, blank=True, verbose_name=__('photo desktop'))
    photo_mobile = models.ImageField(upload_to='images/mobile', null=True, blank=True, verbose_name=__('photo mobile'))

    class Meta:
        abstract = True

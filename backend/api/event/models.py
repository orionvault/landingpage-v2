import uuid
import os
from django.utils.translation import ugettext as _
from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('wallpapers', filename)


class Wallpaper(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    pin_code = models.CharField(max_length=6, verbose_name=_('PIN Code'))
    last_visit = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_('Last visited'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Date created'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('Last update date'))

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Wallpaper')
        verbose_name_plural = _('Wallpapers')

    def __str__(self):
        return self.title


class WallpaperImage(models.Model):
    DEVICES = (
        ('hd', _("HD")),
        ('uhd', _("UHD")),
        ('iphone6', _("iPhone 6")),
        ('iphone6plus', _("iPhone 6+")),
        ('iphone7', _("iPhone 7")),
        ('iphone7plus', _("iPhone 7+")),
        ('iphone8', _("iPhone 8")),
        ('iphone8plus', _("iPhone 8+")),
        ('iphonex', _("iPhone X")),
        ('samsung_s8', _("Samsung S8/S8 Plus")),
        ('samsung_s9', _("Samsung S9/S9 Plus"))
    )

    wallpaper = models.ForeignKey('Wallpaper', on_delete=models.CASCADE,
                                  related_name='wallpaper_images')
    img = models.ImageField(upload_to=get_file_path,
                            verbose_name=_('Image file'))
    device = models.CharField(max_length=12, choices=DEVICES,
                              verbose_name=_('Target device'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Date created'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('Last update date'))

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Wallpaper Image')
        verbose_name_plural = _('Wallpaper Images')

    def __str__(self):
        return str(self.id) + " (" + self.device + ")"

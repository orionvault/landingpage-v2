from django.utils.translation import ugettext as _
from django.db import models


class PresaleOrder(models.Model):
    CURRENCIES = (
        ('usd', _("USD")),
        ('btc', _("BTC")),
        ('eth', _("ETH"))
    )

    INVESTORS = (
        ('individual', _("Individual person")),
        ('investor', _("Accreditated investor")),
        ('fund', _("Fund"))
    )

    first_name = models.CharField(max_length=100, verbose_name=_('First name'))
    last_name = models.CharField(max_length=200, verbose_name=_('Last name'))
    residency = models.CharField(max_length=100, verbose_name=_('Residency'))
    email = models.CharField(max_length=255, verbose_name=_('Email'))
    currency = models.CharField(max_length=3, choices=CURRENCIES, verbose_name=_('Currency'))
    contribution = models.FloatField(verbose_name=_('Contribution'))
    investor_type = models.CharField(max_length=11, choices=INVESTORS, verbose_name=_('Investor type'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Last update date'))

    class Meta:
        ordering = ['last_name']
        verbose_name = _('Presale Order')
        verbose_name_plural = _('Presale Orders')

    def __str__(self):
        return self.first_name + " " + self.last_name

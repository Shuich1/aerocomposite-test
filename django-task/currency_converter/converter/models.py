from django.db import models
from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    short_name = models.CharField(max_length=3, verbose_name=_('short_name'))

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def __str__(self):
        return self.short_name


class CurrencyConversionRate(models.Model):
    from_currency = models.ForeignKey(
        Currency,
        related_name='from_currency',
        on_delete=models.CASCADE,
        verbose_name=_('from_currency')
    )
    to_currency = models.ForeignKey(
        Currency,
        related_name='to_currency',
        on_delete=models.CASCADE,
        verbose_name=_('to_currency')
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name=_('rate')
    )

    class Meta:
        verbose_name = _('ConversionRate')
        verbose_name_plural = _('ConversionRates')

    def __str__(self):
        return f'{self.from_currency.short_name} to ' \
            f'{self.to_currency.short_name}: {self.rate}'

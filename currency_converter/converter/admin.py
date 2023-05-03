from django.contrib import admin

from .models import Currency, CurrencyConversionRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ['short_name']


@admin.register(CurrencyConversionRate)
class CurrencyConvertionRateAdmin(admin.ModelAdmin):
    search_fields = ['from_currency', 'to_currency']

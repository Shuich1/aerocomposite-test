import math

from typing import Dict, Any
from django import forms
from .models import Currency, CurrencyConversionRate


class CurrencyConversionForm(forms.Form):
    amount = forms.DecimalField()
    from_currency = forms.ModelChoiceField(queryset=Currency.objects.all())
    to_currency = forms.ModelChoiceField(queryset=Currency.objects.all())

    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()

        from_currency = cleaned_data.get('from_currency')
        to_currency = cleaned_data.get('to_currency')

        if from_currency == to_currency:
            raise forms.ValidationError("Please select different currencies")

        conversion_rate = CurrencyConversionRate.objects.filter(
            from_currency=from_currency,
            to_currency=to_currency
        ).first()

        if not conversion_rate:
            inverse_conversion_rate = CurrencyConversionRate.objects.filter(
                from_currency=to_currency,
                to_currency=from_currency
            ).first()

            if not inverse_conversion_rate:
                raise forms.ValidationError("Conversion rate not found")

            rate = 1 / inverse_conversion_rate.rate
            cleaned_data['conversion_rate'] = round(
                rate,
                int(-math.floor(math.log10(abs(rate - int(rate))))) + 3
            )
        else:
            rate = conversion_rate.rate
            cleaned_data['conversion_rate'] = round(
                rate,
                int(-math.floor(math.log10(abs(rate - int(rate))))) + 3
            )

        return cleaned_data

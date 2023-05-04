from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import CurrencyConversionForm
from .models import Currency


class CurrencyConverterView(View):
    template_name = 'converter/currency_converter.html'
    form_class = CurrencyConversionForm

    def get(self, request: HttpRequest) -> HttpResponse:
        currencies = Currency.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {
            'currencies': currencies,
            'form': form
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        currencies = Currency.objects.all()
        form = self.form_class(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            conversion_rate = form.cleaned_data['conversion_rate']

            converted_amount = amount * conversion_rate

            return render(request, self.template_name, {
                'currencies': currencies,
                'form': form,
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'converted_amount': converted_amount,
            })

        error_message = ''
        for field_name, error_list in form.errors.items():
            error_message += f'{field_name.capitalize()}: {error_list[0]}.'
        
        from_currency, to_currency = None, None

        if form.data.get('from_currency'):
            from_currency = Currency.objects.get(pk=form.data.get('from_currency'))
        if form.data.get('to_currency'):
            to_currency = Currency.objects.get(pk=form.data.get('to_currency'))

        return render(request, self.template_name, {
            'currencies': currencies,
            'form': form,
            'amount': form.data['amount'],
            'from_currency': from_currency,
            'to_currency': to_currency,
            'error_message': error_message
        })

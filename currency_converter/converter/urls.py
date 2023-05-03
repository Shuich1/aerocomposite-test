from converter import views
from django.urls import path

urlpatterns = [
    path('', views.CurrencyConverterView.as_view()),
]

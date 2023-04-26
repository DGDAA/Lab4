from django.urls import path
from .views import home, tax_rate_view , calculate_total

urlpatterns = [
    path('', home, name='home'),
    path('taxrate/', tax_rate_view, name='tax_rate'),
    path('<number>/', calculate_total, name='calculate_total'),

]

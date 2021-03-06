from django.urls import path
from . import views
from .webhooks import webhook

# All code below taken from boutique ado tutorial
# Indentation applied for flake8 to all paths for consistency
urlpatterns = [
    path(
        '',
        views.checkout,
        name='checkout'
        ),
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'
        ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
        ),
    path(
        'wh/',
        webhook,
        name='webhook'
        ),
]

from django.urls import path
from . import views


# All code below taken from boutique ado tutorial
# Indentation applied for flake8 to all paths for consistency
urlpatterns = [
    path(
        '',
        views.profile,
        name='profile'
        ),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
        ),
]

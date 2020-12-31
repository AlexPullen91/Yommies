from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_scoops, name='scoops'),
    path('bags/', views.all_bags, name='bags'),
    path('addbag/', views.add_bag, name='add_bag'),
    path('addscoop/', views.add_scoop, name='add_scoop'),
]

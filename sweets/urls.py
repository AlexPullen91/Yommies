from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_scoops, name='scoops'),
    path('bags/', views.all_bags, name='bags'),
    path('addbag/', views.add_bag, name='add_bag'),
    path('addscoop/', views.add_scoop, name='add_scoop'),
    path('editbag/<int:bag_id>/', views.edit_bag, name='edit_bag'),
    path('deletebag/<int:bag_id>/', views.delete_bag, name='delete_bag'),
    path('editscoop/<int:scoop_id>/', views.edit_scoop, name='edit_scoop'),
    path('deletescoop/<int:scoop_id>/', views.delete_scoop, name='delete_scoop'),
    path('view/', views.view_all_sweets, name='view_all_sweets'),
]

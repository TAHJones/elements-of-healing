from django.urls import path
from basket import views

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
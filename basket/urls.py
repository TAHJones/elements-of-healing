from django.urls import path
from basket import views

urlpatterns = [
    path('', views.view_basket, name='view_basket')
]
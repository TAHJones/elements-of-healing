from django.urls import path
from appointments import views

urlpatterns = [
    path('', views.appointments, name='appointments'),
]
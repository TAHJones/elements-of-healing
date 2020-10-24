from django.urls import path
from pages import views


urlpatterns = [
    path('', views.home, name='home'),
    path('homeopathy/', views.homeopathy, name='homeopathy'),
    path('about/', views.about, name='about'),
]
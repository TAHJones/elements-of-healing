from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact/success/<email_fromview>', views.successView, name='success'),
]
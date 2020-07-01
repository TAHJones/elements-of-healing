from django.urls import path
from .views import HomePageView, HomeopathyPageView, AboutPageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('homeopathy/', HomeopathyPageView.as_view(), name='homeopathy'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
from django.urls import path
# from .views import HomePageView, HomeopathyPageView, AboutPageView, ContactPageView
from pages import views


# urlpatterns = [
#     path('', HomePageView.as_view(), name='index'),
#     path('homeopathy/', HomeopathyPageView.as_view(), name='homeopathy'),
#     path('about/', AboutPageView.as_view(), name='about'),
#     path('contact/', ContactPageView.as_view(), name='contact'),
# ]

urlpatterns = [
    path('', views.home, name='index'),
    path('homeopathy/', views.homeopathy, name='homeopathy'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
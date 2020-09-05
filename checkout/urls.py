from django.urls import path
from checkout import views
from checkout import webhooks

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhooks.webhook, name='webhook'),
]

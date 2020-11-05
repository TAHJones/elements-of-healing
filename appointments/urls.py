from django.urls import path
from appointments import views

urlpatterns = [
    path('<int:product_id>/', views.appointments, name='appointments'),
    path('purchase_appointment/', views.purchaseAppointment, name='purchase_appointment'),
]
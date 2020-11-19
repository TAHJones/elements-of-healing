from django.urls import path
from appointments import views

urlpatterns = [
    path('<int:product_id>/', views.appointments, name='appointments'),
    path('purchase_appointment/', views.purchaseAppointment, name='purchase_appointment'),
    path('appointment_calendar/', views.appointmentCalendar, name='appointment_calendar'),
    path('appointment_details/<int:appointment_details_id>/', views.appointmentDetails, name='appointment_details'),
]
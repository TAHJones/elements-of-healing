from django.shortcuts import render
from .forms import AppointmentForm


def appointments(request):
    appointmentForm = AppointmentForm()
    return render(request, 'appointments/appointments.html', {'appointmentForm': appointmentForm})

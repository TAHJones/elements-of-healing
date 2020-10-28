from django.shortcuts import render
from .forms import AppointmentForm


def appointments(request):
    form = AppointmentForm()
    return render(request, 'appointments/appointments.html', {'form': form})

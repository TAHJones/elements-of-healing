from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import AppointmentForm
from appointments.models import BookAppointment
from products.models import Product
from .utils import Calendar
from datetime import datetime
from django.utils.safestring import mark_safe


def appointments(request, product_id):
    """ A view to request an appointment at a specified date & time """
    bookings = list(BookAppointment.objects.all().values())
    if request.method == 'GET':
        form = AppointmentForm()
    else:
        currentMonth = datetime.datetime.now().date().strftime('%m/%y')
        day = datetime.datetime.now().date().strftime('%d')
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cust_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            host_email = settings.DEFAULT_FROM_EMAIL
            # email_to = settings.EMAIL_HOST_USER
            for item in bookings:
                if item['date'][3:8] == currentMonth:
                    if int(item['date'][0:2]) < int(day):
                        BookAppointment(id=item['id']).delete()
                    elif item['time'] == time and item['date'] == date:
                        messages.error(request, 'Sorry, that appointment time has already been taken. Please select another time.')
                        return redirect(reverse('appointments', args=[product_id]))
            form.save()
            appointment_details = {
                'name': name,
                'cust_email': cust_email,
                'message': message,
                'date': date,
                'time': time,
                'host_email': host_email,
            }
            request.session['appointment_id'] = product_id
            request.session['appointment_details'] = appointment_details
            return redirect(reverse('purchase_appointment'))
    return render(request, 'appointments/appointments.html', {'form': form})


def purchaseAppointment(request):
    """ A view to confirm appointment details then add to shopping basket """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can purchase an appointment.')
        return redirect(reverse('appointments'))

    appointment = get_object_or_404(Product, pk=request.session['appointment_id'])

    context = {
        'appointment': appointment,
        'appointment_details': request.session['appointment_details']
    }

    return render(request, 'appointments/purchase_appointment.html', context)


def appointmentCalendar(request):
    """  Displays a calendar of all appointments """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you must have admin privileges to view appointment bookings')
        return redirect(reverse('appointments'))

    # bookings = list(BookAppointment.objects.all().values())
    d = datetime.today()
    cal = Calendar(d.year, d.month)
    # cal = Calendar(2016, 11)

    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    calendar = mark_safe(html_cal)
    print(calendar)

    context = {
        'calendar': calendar,
    }

    return render(request, 'appointments/appointment_calendar.html', context)

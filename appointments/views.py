from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import AppointmentForm
from appointments.models import AppointmentsCalendar
from appointments.googleCalendar import addGoogleCalendarEvent, updateGoogleCalendarEvent, deleteGoogleCalendarEvent
from products.models import Product
from .utils import Calendar, convertToDatetime, get_date, prev_month, next_month, get_footer
from datetime import datetime
from django.utils.safestring import mark_safe
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from json import dumps


def appointments(request, product_id):
    """ A view to request an appointment at a specified date & time """
    basket = request.session.get('basket', {})
    for item_id in basket.keys():
        if int(item_id) == 1 or int(item_id) == 2:
            messages.error(request, 'Error, you already have an appointment in your basket')
            return redirect(reverse('view_basket'))

    appointments = list(AppointmentsCalendar.objects.all().values())
    username = request.user.username
    email = request.user.email
    if request.method == 'GET':
        form = AppointmentForm(initial={'name': username, 'email': email})
    else:
        currentMonth = datetime.now().month
        currentYear = datetime.now().date().strftime('%y')
        nextYear = int(currentYear) + 1
        if currentMonth < 3:
            minMonth = currentMonth + 10
        else:
            minMonth = currentMonth - 2

        minDate = f'{minMonth}/{currentYear}'
        day = datetime.now().date().strftime('%d')
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cust_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            host_email = settings.DEFAULT_FROM_EMAIL
            for item in appointments:
                if item['date_str'][3:8] == minDate:
                    if int(item['date_str'][0:2]) < int(day):
                        AppointmentsCalendar(id=item['id']).delete()

                if item['time'] == time and item['date_str'] == date:
                    messages.error(request, 'Sorry, that appointment time has already been taken. Please select another time.')
                    return redirect(reverse('appointments', args=[product_id]))
                elif item['user'] == username and item['date_str'] == date:
                    messages.error(request, 'Sorry, you cannot book more than one appointment on the same day')
                    return redirect(reverse('appointments', args=[product_id]))

            getDate = []
            for item in date.split('/'):
                getDate.append(int(item))

            fourDigitYear = getDate[2]
            year_str = str(fourDigitYear)
            year_len = len(year_str)
            year = int(year_str[year_len - 2: year_len])
            month = getDate[1]

            if year > nextYear or month >= currentMonth and year == nextYear:
                messages.error(request, 'Sorry, you cannot book an appointment more than a year in advance.')
                return redirect(reverse('appointments', args=[product_id]))

            appointment_details = {
                'user': username,
                'name': name,
                'cust_email': cust_email,
                'message': message,
                'date': date,
                'time': time,
                'host_email': host_email,
                'confirmed': False,
                'eventId': None,
            }

            request.session['appointment_details'] = appointment_details
            return redirect(reverse('purchase_appointment', args=[product_id]))
    context = {
        'form': form
    }
    return render(request, 'appointments/appointments.html', context)


def purchaseAppointment(request, product_id):
    """ A view to confirm appointment details then add to shopping basket """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can purchase an appointment.')
        return redirect(reverse('appointments', args=[product_id]))

    appointment = get_object_or_404(Product, pk=product_id)

    context = {
        'appointment': appointment,
        'appointment_details': request.session['appointment_details']
    }

    return render(request, 'appointments/purchase_appointment.html', context)


class appointmentCalendar(generic.ListView):
    model = AppointmentsCalendar
    template_name = 'appointments/appointment_calendar.html'
    success_url = reverse_lazy("appointment_calendar")

    def get_context_data(self, **kwargs):
        """ displays calendar of users appointments or all appointments if user is superuser """
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        if self.request.user.is_superuser:
            cal = Calendar(d.year, d.month)
        elif self.request.user.is_authenticated:
            user = self.request.user.username
            cal = Calendar(d.year, d.month, user)

        html_cal = cal.formatmonth(withyear=True)
        html_cal += get_footer()
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


@login_required
def appointmentDetails(request,  appointment_details_id):
    """ Displays individual calendar appointment details """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users are allowed do that.')
        return redirect(reverse('home'))

    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id).values()[0]

    context = {
        'appointment_details': appointment_details,
    }

    return render(request, 'appointments/appointment_details.html', context)


@login_required
def confirmAppointment(request, appointment_details_id):
    """ Allows superuser to confirms individual calendar appointment details """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only users with admin privileges can confirm appointments.')
        return redirect(reverse('home'))

    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id)
    appointment = appointment_details.values()[0]
    if appointment['confirmed']:
        messages.error(request, 'The selected appointment has already been confirmed.')
        return redirect(reverse('appointment_details', args=[appointment_details_id]))
    user = appointment['user']
    startTime = convertToDatetime(appointment['date_str'], appointment['time'])
    googleCalendarEvent = addGoogleCalendarEvent(startTime, appointment['user'], appointment['email'], appointment['message'])
    appointment_details.update(confirmed=True, eventId=googleCalendarEvent['id'])
    appointment = appointment_details.values()[0]
    appointmentInSession = request.session.get('appointment_details', None)
    if appointmentInSession:
        if appointment['id'] == appointmentInSession['id'] and appointment['user'] == appointmentInSession['user']:
            if appointment['time'] == appointmentInSession['time'] and appointment['date_str'] == appointmentInSession['date']:
                appointmentInSession['confirmed'] = appointment['confirmed']
                if appointmentInSession['confirmed']:
                    appointmentInSession['eventId'] = appointment['eventId']

    messages.success(request, f'Appointment for {user} has been confirmed & added to your Google Calendar')
    request.session['appointment_details'] = appointmentInSession
    context = {
        'appointment_details': appointment,
    }

    return render(request, 'appointments/appointment_details.html', context)


@login_required
def updateAppointment(request, appointment_details_id):
    """ Allows superuser to update individual calendar appointment details """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only users with admin privileges can update appointments.')
        return redirect(reverse('appointment_calendar'))
    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id)
    allAppointments = list(AppointmentsCalendar.objects.all().values())
    appointment = appointment_details.values()[0]
    eventId = appointment['eventId']
    confirmed = appointment['confirmed']
    user = appointment['user']
    date_str = appointment['date_str']
    if request.method == 'GET':
        email = appointment['email']
        message = appointment['message']
        time = appointment['time']
        form = AppointmentForm(initial={'name': user, 'email': email, 'message': message})
        dateTime = {'day': date_str[0:2], 'month': date_str[3:5], 'year': date_str[6:10], 'time': time[0:2], 'date': date_str}
        jsData = dumps(dateTime)
    else:
        form = AppointmentForm(request.POST)
        appointment = {}
        if form.is_valid():
            appointment['name'] = form.cleaned_data['name']
            appointment['email'] = form.cleaned_data['email']
            appointment['message'] = form.cleaned_data['message']
            appointment['date_str'] = form.cleaned_data['date']
            appointment['time'] = form.cleaned_data['time']
            appointment['date'] = convertToDatetime(appointment['date_str'], appointment['time'])
            for item in allAppointments:
                if item['time'] == appointment['time'] and item['date_str'] == appointment['date_str']:
                    messages.error(request, 'Sorry, that appointment time has already been taken. Please select another time.')
                    return redirect(reverse('appointment_details', args=[appointment_details_id]))
                elif item['user'] == user and item['date_str'] == appointment['date_str']:
                    if appointment['date_str'] !=  date_str:
                        messages.error(request, 'Sorry, you cannot book more than one appointment per user on the same day')
                        return redirect(reverse('appointment_details', args=[appointment_details_id]))
            messages.success(request, 'The selected appointment has been updated.')
            if confirmed:
                updateGoogleCalendarEvent(appointment['date'], user, appointment['email'], eventId, appointment['message'])
            appointment_details.update(**appointment)
            return redirect(reverse('appointment_details', args=[appointment_details_id]))
        return redirect(reverse('appointment_details', args=[appointment_details_id]))

    context = {
        'jsData': jsData,
        'form': form
    }

    return render(request, 'appointments/update_appointment.html', context)


@login_required
def deleteAppointment(request,  appointment_details_id):
    """ Allows superuser to delete individual calendar appointment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only users with admin privileges can delete appointments.')
        return redirect(reverse('home'))

    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id)
    appointment = appointment_details.values()[0]
    eventId = appointment['eventId']
    confirmed = appointment['confirmed']
    messages.success(request, 'The selected appointment has been deleted from your calendar.')
    appointment_details.delete()

    if confirmed:
        deleteGoogleCalendarEvent(eventId)
    return redirect(reverse('products'))

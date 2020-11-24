from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import AppointmentForm
from appointments.models import AppointmentsCalendar
from products.models import Product
from .utils import Calendar
from datetime import datetime, timedelta
from django.utils.safestring import mark_safe
from django.views import generic
from django.urls import reverse_lazy
import calendar


def appointments(request, product_id):
    """ A view to request an appointment at a specified date & time """
    appointments = list(AppointmentsCalendar.objects.all().values())
    if request.method == 'GET':
        username = request.user.username
        email = request.user.email
        form = AppointmentForm(initial={'name': username, 'email': email})
    else:
        currentMonth = datetime.now().month
        currentYear = datetime.now().date().strftime('%y')
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
            # email_to = settings.EMAIL_HOST_USER
            for item in appointments:
                if item['date_str'][3:8] == minDate:
                    if int(item['date_str'][0:2]) < int(day):
                        AppointmentsCalendar(id=item['id']).delete()
                    elif item['time'] == time and item['date_str'] == date:
                        messages.error(request, 'Sorry, that appointment time has already been taken. Please select another time.')
                        return redirect(reverse('appointments', args=[product_id]))
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


class appointmentCalendar(generic.ListView):
    model = AppointmentsCalendar
    template_name = 'appointments/appointment_calendar.html'
    success_url = reverse_lazy("appointment_calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        html_cal += get_footer()
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_footer():
    currentYear = datetime.now().date().strftime('%Y')
    footer = f'</table><footer><div class="footer-copyright"><div id="copyRight">2011 - {currentYear} © Thomas Jones - All Rights Reserved</div></div></footer>'
    return footer


def appointmentDetails(request,  appointment_details_id):
    """ Displays individual calendar appointment details """
    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id).values()[0]

    context = {
        'appointment_details': appointment_details,
    }

    return render(request, 'appointments/appointment_details.html', context)


def confirmAppointment(request, appointment_details_id):
    """ Allows superuser to confirms individual calendar appointment details """
    appointment_details = AppointmentsCalendar.objects.filter(pk=appointment_details_id)
    appointment_details.update(confirmed=True)
    appointment = appointment_details.values()[0]
    name = appointment['name']
    messages.success(request, f'Appointment for {name} has been confirmed')

    context = {
        'appointment': appointment,
    }

    return render(request, 'appointments/appointment_details.html', context)

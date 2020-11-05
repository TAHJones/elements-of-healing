from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import AppointmentForm
from products.models import Product


def appointments(request, product_id):
    if request.method == 'GET':
        form = AppointmentForm()
    else:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cust_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            host_email = settings.DEFAULT_FROM_EMAIL
            # email_to = settings.EMAIL_HOST_USER
            appointment_details = {
                'name': name,
                'cust_email': cust_email,
                'message': message,

                'date': date,
                'time': time,
                'host_email': host_email,
            }
            subject = render_to_string(
                'appointments/confirmation_emails/confirmation_email_subject.txt',
                {'email': appointment_details})
            body = render_to_string(
                'appointments/confirmation_emails/confirmation_email_body.txt',
                {'email': appointment_details})
            try:
                # forward message from customer to host email address
                send_mail(name, message, cust_email, [host_email])
                messages.success(request, f'Your appointment request has been received! A confirmation email will be sent to {cust_email}.')
                # send confirmation message from host to customer email address
                send_mail(subject, body, host_email, [cust_email])
            except Exception as e:
                messages.error(request, 'Sorry, there was a problem sending your appointment request. Please try again.')
                return HttpResponse(content=e, status=400)
            request.session['appointment_id'] = product_id
            request.session['appointment_details'] = appointment_details
            return redirect(reverse('purchase_appointment'))
    return render(request, 'appointments/appointments.html', {'form': form})


def purchaseAppointment(request):
    """ A view to purchase an appointment """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only registered users can purchase an appointment.')
        return redirect(reverse('appointments'))

    appointment = get_object_or_404(Product, pk=request.session['appointment_id'])

    context = {
        'appointment': appointment,
        'appointment_details': request.session['appointment_details']
    }

    return render(request, 'appointments/purchase_appointment.html', context)

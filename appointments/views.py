from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import AppointmentForm


def appointments(request):
    if request.method == 'GET':
        form = AppointmentForm()
    else:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cust_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # print()
            print(type(message))
            date = form.cleaned_data['date']
            print(type(date))
            time = form.cleaned_data['time']
            print(type(time))
            host_email = settings.DEFAULT_FROM_EMAIL
            # email_to = settings.EMAIL_HOST_USER
            email = {
                'name': name,
                'cust_email': cust_email,
                'message': message,
                'date': date,
                'time': time,
                'host_email': host_email,
            }
            subject = render_to_string(
                'appointments/confirmation_emails/confirmation_email_subject.txt',
                {'email': email})
            body = render_to_string(
                'appointments/confirmation_emails/confirmation_email_body.txt',
                {'email': email})
            try:
                # forward message from customer to host email address
                send_mail(name, message, cust_email, [host_email])
                messages.success(request, f'Your appointment request has been received! A confirmation email will be sent to {cust_email}.')
                # send confirmation message from host to customer email address
                send_mail(subject, body, host_email, [cust_email])
            except Exception as e:
                messages.error(request, 'Sorry, there was a problem sending your appointment request. Please try again.')
                return HttpResponse(content=e, status=400)
            return redirect(reverse('appointments'))
    return render(request, 'appointments/appointments.html', {'form': form})

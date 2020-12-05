from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from datetime import datetime
from appointments.utils import convertToDatetime
from .forms import ContactForm
from .models import Contact


def contact(request):
    """ A view to send an email enquires about homeopathic services & information """
    contacts = list(Contact.objects.all().values())
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cust_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = datetime.today()
            year = datetime.today().year
            for item in contacts:
                if year - item['year'] > 1:
                    Contact(id=item['id']).delete()

            Contact(
                name=name,
                email=cust_email,
                message=message,
                date=date,
                year=year,
            ).save()

            host_email = settings.DEFAULT_FROM_EMAIL
            email = {
                'name': name,
                'cust_email': cust_email,
                'message': message,
                'host_email': host_email,
            }
            subject = render_to_string(
                'confirmation_emails/confirmation_email_subject.txt',
                {'email': email})
            body = render_to_string(
                'confirmation_emails/confirmation_email_body.txt',
                {'email': email})
            try:
                # forward message from customer to host email address
                send_mail(name, message, cust_email, [host_email])
                messages.success(request, f'Your message has been received! A confirmation email will be sent to {cust_email}.')
                # send confirmation message from host to customer email address
                send_mail(subject, body, host_email, [cust_email])
            except Exception as e:
                messages.error(request, 'Sorry, there was a problem sending your message. Please try again.')
                return HttpResponse(content=e, status=400)
            return redirect(reverse('contact'))

        context = {
            'banner': True,
            'form': form,
        }

    return render(request, 'contact/contact.html', context)

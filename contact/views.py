from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # send email code goes here
#             return HttpResponse('Thanks for contacting us!')
#     else:
#         form = ContactForm()

#     return render(request, 'contact/contact.html', {'form': form})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']
            email_to = settings.DEFAULT_FROM_EMAIL
            try:
                send_mail(name, message, email_from, [email_to])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success', email_from)
    return render(request, 'contact/contact.html', {'form': form})


def successView(request, email_from):
    messages.success(request, f'Your message has been recieved! A confirmation email will be sent to {email_from}.')
    # return HttpResponse('Success! Thank you for your message.')
    # return render(request, 'contact/contact.html', {'form': form})
    return render(request, 'contact/success.html')

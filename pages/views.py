# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


class HomeopathyPageView(TemplateView):
    template_name = 'homeopathy.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'

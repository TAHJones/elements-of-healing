from django.shortcuts import render, redirect
# from django.shortcuts import render
# from django.views.generic import TemplateView

# Create your views here.

# class HomePageView(TemplateView):
#     template_name = 'index.html'


def home(request):
    context = {
        'banner': True
    }
    return render(request, "index.html", context)


# class HomeopathyPageView(TemplateView):
#     template_name = 'homeopathy.html'


def homeopathy(request):
    context = {
        'banner': True
    }
    return render(request, "homeopathy.html", context)

# class AboutPageView(TemplateView):
#     template_name = 'about.html'


def about(request):
    context = {
        'banner': True
    }
    return render(request, "about.html", context)


# class ContactPageView(TemplateView):
#     template_name = 'contact.html'


def contact(request):
    context = {
        'banner': True
    }
    return render(request, "contact.html", context)

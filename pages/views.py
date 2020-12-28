from django.shortcuts import render
from datetime import datetime

currentYear = datetime.now().date().strftime('%y')


def home(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "pages/index.html", context)


def homeopathy(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "pages/homeopathy.html", context)


def consultation(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "pages/consultation.html", context)


def about(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "pages/about.html", context)

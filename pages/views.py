from django.shortcuts import render
from datetime import datetime

currentYear = datetime.now().date().strftime('%y')


def home(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "index.html", context)


def homeopathy(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "homeopathy.html", context)


def about(request):
    context = {
        'banner': True,
        'currentYear': currentYear,
    }
    return render(request, "about.html", context)

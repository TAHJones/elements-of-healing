from django.shortcuts import render


def home(request):
    context = {
        'banner': True
    }
    return render(request, "index.html", context)


def homeopathy(request):
    context = {
        'banner': True
    }
    return render(request, "homeopathy.html", context)


def about(request):
    context = {
        'banner': True
    }
    return render(request, "about.html", context)



def contact(request):
    context = {
        'banner': True
    }
    return render(request, "contact.html", context)

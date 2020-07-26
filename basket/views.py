from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view that renders the shopping basket page """

    return render(request, 'basket.html')

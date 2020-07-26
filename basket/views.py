from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    """ A view that renders the shopping basket page """

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """ Add a specific quantity of a selected product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

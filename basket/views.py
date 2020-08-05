from django.shortcuts import render, redirect

# Create your views here.


def view_basket(request):
    """ A view that renders the shopping basket page """

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """ Add a specific quantity of a selected product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    potency = None
    if 'potency' in request.POST:
        potency = request.POST['potency']

    basket = request.session.get('basket', {})

    if potency:
        if item_id in list(basket.keys()):
            if potency in basket[item_id]['items_by_potency'].keys():
                basket[item_id]['items_by_potency'][potency] += quantity
            else:
                basket[item_id]['items_by_potency'][potency] = quantity
        else:
            basket[item_id] = {'items_by_potency': {potency: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)

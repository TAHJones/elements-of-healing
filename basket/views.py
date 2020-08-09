from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_basket(request):
    """A view that renders the shopping basket page"""

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """Add a specific quantity of a selected product to the shopping basket"""

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


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_potency'][size] = quantity
        else:
            del basket[item_id]['items_by_potency'][size]
            if not basket[item_id]['items_by_potency']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_potency'][size]
            if not basket[item_id]['items_by_potency']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

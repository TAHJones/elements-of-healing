from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):
    """A view that renders the shopping basket page"""

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """Add a specific quantity of a selected product to the shopping basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    potency = None
    if 'product_potency' in request.POST:
        potency = request.POST['product_potency']

    basket = request.session.get('basket', {})

    if potency:
        if item_id in list(basket.keys()):
            if potency in basket[item_id]['items_by_potency'].keys():
                basket[item_id]['items_by_potency'][potency] += quantity
                messages.success(request, f'Updated potency {potency.upper()} {product.name} quantity to {basket[item_id]["items_by_potency"][potency]}')
            else:
                basket[item_id]['items_by_potency'][potency] = quantity
                messages.success(request, f'Added potency {potency.upper()} {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_potency': {potency: quantity}}
            messages.success(request, f'Added potency {potency.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    potency = None
    if 'product_potency' in request.POST:
        potency = request.POST['product_potency']
    basket = request.session.get('basket', {})

    if potency:
        if quantity > 0:
            basket[item_id]['items_by_potency'][potency] = quantity
            messages.success(request, f'Updated potency {potency.upper()} {product.name} quantity to {basket[item_id]["items_by_potency"][potency]}')
        else:
            del basket[item_id]['items_by_potency'][potency]
            if not basket[item_id]['items_by_potency']:
                basket.pop(item_id)
                messages.success(request, f'Removed potency {potency.upper()} {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        potency = None
        if 'product_product' in request.POST:
            potency = request.POST['product_size']
        basket = request.session.get('basket', {})

        if potency:
            del basket[item_id]['items_by_potency'][potency]
            if not basket[item_id]['items_by_potency']:
                basket.pop(item_id)
            messages.success(request, f'Removed potency {potency.upper()} {product.name} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

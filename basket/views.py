from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
from products.models import Product
from appointments.models import AppointmentsCalendar
from appointments.utils import convertToDatetime
from appointments.googleCalendar import deleteGoogleCalendarEvent


def view_basket(request):
    """A view that renders the shopping basket page"""

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """Add a specific quantity of a selected product to the shopping basket"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    potency = None
    if 'potency' in request.POST:
        potency = request.POST['potency']

    basket = request.session.get('basket', {})
    if int(item_id) == 1 or int(item_id) == 2:
        for k in basket.keys():
            if int(k) == 1 or int(k) == 2:
                messages.error(request, 'Error, you already have an appointment in your basket')
                return redirect(reverse('view_basket'))

    if product.category.friendly_name == "Appointments":
        basket[item_id] = quantity

        appointment_details = request.session.get('appointment_details', {})
        user = appointment_details['user']
        name = appointment_details['name']
        cust_email = appointment_details['cust_email']
        message = appointment_details['message']
        date_str = appointment_details['date']
        time = appointment_details['time']
        date = convertToDatetime(date_str, time)

        AppointmentsCalendar(
            user=user,
            name=name,
            email=cust_email,
            message=message,
            date=date,
            date_str=date_str,
            time=time
        ).save()

        appointments = list(AppointmentsCalendar.objects.all().values())
        for item in appointments:
            if item['time'] == time and item['date_str'] == date_str:
                request.session['appointment_details']['id'] = item['id']

    elif potency:
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
    confirmed = request.session['appointment_details']['confirmed']
    if confirmed:
        eventId = request.session['appointment_details']['eventId']
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
            if product.category.friendly_name == "Appointments":
                basket.pop(item_id)
                if confirmed is True:
                    deleteGoogleCalendarEvent(eventId)
                    AppointmentsCalendar(id=request.session['appointment_details']['id']).delete()
                    messages.success(request, 'Removed appointment from your basket')
                    request.session['appointment_details']['confirmed'] = False
                    request.session['appointment_details']['eventId'] = None
                elif confirmed is not True:
                    AppointmentsCalendar(id=request.session['appointment_details']['id']).delete()
                    messages.success(request, 'Removed appointment from your basket')
            else:
                basket.pop(item_id)
                messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

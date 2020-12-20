from django.shortcuts import render, redirect, reverse
import json


def view_cart(request):
    """ A view to render shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add a quantity of the sweet bags to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    bag_choice = request.POST.get('bag_choice')
    item_id = json.loads(bag_choice)['id']
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified sweet bag """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

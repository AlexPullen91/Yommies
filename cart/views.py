from django.shortcuts import render, redirect
import json


def view_cart(request):
    """ A view to render shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add a quantity of the sweet bags to the shopping cart """

    quantity = 1
    bag_choice = request.POST.get('bag_choice')
    item_id = json.loads(bag_choice)['id']
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    print(bag_choice)
    print(item_id)
    print(request.session['cart'])

    return redirect(redirect_url)

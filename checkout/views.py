from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hk5RbLKcHuxhv74NsfTsm30k4QWIVXDxDArdX6m3cjByzBZYKa9hf3nEUHiv3gSJJL5yD8FJ9vLjtFdCMq13RoJ00yZ07nb0g',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

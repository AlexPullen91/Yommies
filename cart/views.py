from django.shortcuts import render


def view_cart(request):
    """ A view to render shopping cart contents page """
    return render(request, 'cart/cart.html')

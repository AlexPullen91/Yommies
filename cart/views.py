from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to render shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request):
    """ Add a quantity of the sweet bags to the shopping cart """

    bag_choice = request.POST.get('bag_choice')
    redirect_url = request.POST.get('redirect_url')

    print(bag_choice)

    return redirect(redirect_url)

from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from sweets.models import Bags, Scoops, Category
import json


def view_cart(request):
    """ A view to render shopping cart contents page """
    return render(request, 'cart/cart.html')


def add_scoops_to_bag(request):

    quantity = int(request.POST.get('quantity'))
    scoop_one = request.POST.get('scoop_one')
    scoop_one_name = json.loads(scoop_one)['name']
    scoop_one_id = json.loads(scoop_one)['id']
    scoop_two = request.POST.get('scoop_two')
    scoop_two_name = json.loads(scoop_two)['name']
    scoop_two_id = json.loads(scoop_two)['id']
    scoop_three = request.POST.get('scoop_three')
    scoop_three_name = json.loads(scoop_three)['name']
    scoop_three_id = json.loads(scoop_three)['id']
    scoop_four = request.POST.get('scoop_four')
    scoop_four_name = json.loads(scoop_four)['name']
    scoop_four_id = json.loads(scoop_four)['id']
    scoop_five = request.POST.get('scoop_five')
    scoop_five_name = json.loads(scoop_five)['name']
    scoop_five_id = json.loads(scoop_five)['id']
    scoop_six = request.POST.get('scoop_six')
    scoop_six_name = json.loads(scoop_six)['name']
    scoop_six_id = json.loads(scoop_six)['id']
    scoop_seven = request.POST.get('scoop_seven')
    scoop_seven_name = json.loads(scoop_seven)['name']
    scoop_seven_id = json.loads(scoop_seven)['id']
    scoop_eight = request.POST.get('scoop_eight')
    scoop_eight_name = json.loads(scoop_eight)['name']
    scoop_eight_id = json.loads(scoop_eight)['id']
    scoop_nine = request.POST.get('scoop_nine')
    scoop_nine_name = json.loads(scoop_nine)['name']
    scoop_nine_id = json.loads(scoop_nine)['id']
    scoop_ten = request.POST.get('scoop_ten')
    scoop_ten_name = json.loads(scoop_ten)['name']
    scoop_ten_id = json.loads(scoop_ten)['id']

    ten_scoops = [scoop_one_id, scoop_two_id, scoop_three_id, scoop_four_id, scoop_five_id, scoop_six_id, scoop_seven_id, scoop_eight_id, scoop_nine_id, scoop_ten_id]

    custom_mix = Bags(name='CUSTOM MIX', is_vegetarian=True, description='Custom selection of pick n mix', weight='1KG', price=12.00)
    custom_mix.save()
    scoop_qty = []
    for scoop in ten_scoops:
        custom_mix.scoops.add(scoop)
        # if ten_scoops in list(custom_mix.scoops.all()):
        #     scoop_qty += scoop_qty
    redirect_url = request.POST.get('redirect_url')

    print(custom_mix)
    print(ten_scoops)
    print(scoop_qty)

    return redirect(redirect_url)


def add_to_cart(request):
    """ Add a quantity of the sweet bags to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    bag_choice = request.POST.get('bag_choice')
    bag_name = json.loads(bag_choice)['name']
    bag_item_id = json.loads(bag_choice)['id']
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if bag_item_id in list(cart.keys()):
        cart[bag_item_id] += quantity
        messages.success(request, f'{bag_name} quantity updated to {cart[bag_item_id]}!')
    else:
        cart[bag_item_id] = quantity
        messages.success(request, f'{bag_name} have been added to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified sweet bag """

    bag = get_object_or_404(Bags, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'{bag.name} quantity updated to {cart[item_id]} !')
    else:
        cart.pop(item_id)
        messages.success(request, f'{bag.name} removed from your cart.')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove item from the shopping cart """

    try:
        bag = get_object_or_404(Bags, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'{bag.name} removed from your cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

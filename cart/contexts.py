from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sweets.models import Bags


# Following code adapted from boutique ado tutorial
def cart_contents(request):
    """ Provides access to the shopping cart across the app """

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        bag_choice = get_object_or_404(Bags, pk=item_id)
        scoops = bag_choice.scoops.all()
        total += quantity * bag_choice.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'bag_choice': bag_choice,
            'scoops': scoops,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

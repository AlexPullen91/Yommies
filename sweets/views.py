from django.shortcuts import render
from .models import Scoops, Bags


def all_scoops(request):
    """ A view to show scoops page """

    scoops = Scoops.objects.all()

    context = {
        'scoops': scoops,
    }

    return render(request, 'sweets/scoops.html', context)


def all_bags(request):
    """ A view to show bags page """

    bags = Bags.objects.all()

    context = {
        'bags': bags,
    }

    return render(request, 'sweets/bags.html', context)

from django.shortcuts import render
from .models import Scoops


def all_scoops(request):
    """ A view to show scoops page """

    scoops = Scoops.objects.all()

    context = {
        'scoops': scoops,
    }

    return render(request, 'scoops/scoops.html', context)

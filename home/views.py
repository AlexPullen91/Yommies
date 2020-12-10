from django.shortcuts import render
from .models import Card


def index(request):
    """ A view to return the index page """

    card = Card.objects.all()

    context = {
        'card': card,
    }

    return render(request, 'home/index.html', context)

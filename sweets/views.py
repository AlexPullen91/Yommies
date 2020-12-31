from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Scoops, Bags
from .forms import BagsForm, ScoopsForm


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


def add_bag(request):
    """ Add a bag to the store """
    if request.method == 'POST':
        form = BagsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bag has been successfully added.')
            return redirect(reverse('add_bag'))
        else:
            messages.error(request, 'Failed to add bag. Please make sure the form is valid.')
    else:
        form = BagsForm()

    template = 'sweets/add_bag.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_scoop(request):
    """ Add a new scoop to the store """
    if request.method == 'POST':
        form = ScoopsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The scoop has been successfully added.')
            return redirect(reverse('add_scoop'))
        else:
            messages.error(request, 'Failed to add scoop. Please make sure the form is valid.')
    else:
        form = ScoopsForm()

    template = 'sweets/add_scoop.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

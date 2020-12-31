from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_bag(request):
    """ Add a bag to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BagsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bag has been successfully added.')
            return redirect(reverse('view_all_sweets'))
        else:
            messages.error(
                request,
                'Failed to add bag. Please make sure the form is valid.'
                )
    else:
        form = BagsForm()

    template = 'sweets/add_bag.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_scoop(request):
    """ Add a new scoop to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ScoopsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The scoop has been successfully added.')
            return redirect(reverse('view_all_sweets'))
        else:
            messages.error(
                request,
                'Failed to add scoop. Please make sure the form is valid.'
                )
    else:
        form = ScoopsForm()

    template = 'sweets/add_scoop.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_bag(request, bag_id):
    """ Edit a bag in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    bag = get_object_or_404(Bags, pk=bag_id)
    if request.method == 'POST':
        form = BagsForm(request.POST, request.FILES, instance=bag)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bag updated successfully.')
            return redirect('view_all_sweets')
        else:
            messages.error(
                request,
                'Failed to update bag. Please make sure the form is valid.'
                )
    else:
        form = BagsForm(instance=bag)
        messages.info(request, f'You are editing {bag.name}')

    template = 'sweets/edit_bag.html'
    context = {
        'form': form,
        'bag': bag,
    }

    return render(request, template, context)


@login_required
def edit_scoop(request, scoop_id):
    """ Edit a scoop in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    scoop = get_object_or_404(Scoops, pk=scoop_id)
    if request.method == 'POST':
        form = ScoopsForm(request.POST, request.FILES, instance=scoop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scoop updated successfully.')
            return redirect('view_all_sweets')
        else:
            messages.error(
                request,
                'Failed to update scoop. Please make sure the form is valid.'
                )
    else:
        form = ScoopsForm(instance=scoop)
        messages.info(request, f'You are editing {scoop.name}')

    template = 'sweets/edit_scoop.html'
    context = {
        'form': form,
        'scoop': scoop,
    }

    return render(request, template, context)


@login_required
def delete_bag(request, bag_id):
    """ Delete bag from the store """
    if not request.user.is_superuser:
        messages.error(
            request,
            'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    bag = get_object_or_404(Bags, pk=bag_id)
    bag.delete()
    messages.success(request, 'Bag deleted!')
    return redirect(reverse('view_all_sweets'))


@login_required
def delete_scoop(request, scoop_id):
    """ Delete scoop from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Forbidden! Only store owners can do that.')
        return redirect(reverse('home'))

    scoop = get_object_or_404(Scoops, pk=scoop_id)
    scoop.delete()
    messages.success(request, 'Scoop deleted!')
    return redirect(reverse('view_all_sweets'))


@login_required
def view_all_sweets(request):
    """ A view for management to display all sweets in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'This action is forbidden. Only store owners can do that.'
            )
        return redirect(reverse('home'))

    bags = Bags.objects.all()
    scoops = Scoops.objects.all()

    context = {
        'scoops': scoops,
        'bags': bags,
    }

    return render(request, 'sweets/all_sweets.html', context)

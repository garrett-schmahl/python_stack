from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Network, Show

def landing(request):
    return redirect('/shows')


def all_shows_render(request):
    context ={
        'all_shows': Show.objects.all()
    }
    return render(request, 'main_app/index.html', context)


def new_show(request):
    context = {
        'all_networks': Network.objects.all(),
    }
    return render(request, 'main_app/show_new.html', context)


def create_show(request):
    errors = Show.objects.validator(request.POST, Show.objects.all())
    for key, value in errors.items():
        messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show=Show.objects.create(
            name=request.POST['show_name_input'],
            release_date=request.POST['show_date_input'],
            network=Network.objects.get(id=request.POST['network_select']),
            description=request.POST['show_description']
        )
        print(new_show.release_date)
        return redirect(f'/shows/{new_show.id}')


def edit_show(request, show_id):
    current_show = Show.objects.get(id=show_id)
    context = {
        'all_networks': Network.objects.all(),
        'show_to_edit': Show.objects.get(id=show_id),
    }
    return render(request, 'main_app/show_edit.html', context)


def update_show(request, show_id):
    errors = Show.objects.validator(request.POST, Show.objects.all())
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        update_show = Show.objects.get(id=show_id)
        update_show.name = request.POST['show_name_input']
        update_show.release_date = request.POST['show_date_input']
        update_show.network = Network.objects.get(id=request.POST['network_select'])
        update_show.description = request.POST['show_description']
        update_show.save()
        return redirect(f'/shows/{show_id}')


def show_detail(request, show_id):
    context={
        "show":Show.objects.get(id=show_id)
    }
    return render(request, 'main_app/show_detail.html', context)


def delete_show(request, show_id):
    show_to_delete=Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')
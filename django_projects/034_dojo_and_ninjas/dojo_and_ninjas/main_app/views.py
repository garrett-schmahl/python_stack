from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)


def process_new(request):
    if request.POST["submit_type"] == "dojo":
        Dojo.objects.create(
            dojo_name=request.POST['dojo_name'], 
            dojo_city=request.POST['dojo_city'], 
            dojo_state=request.POST['dojo_state'])
    if request.POST["submit_type"] == "ninja":
        Ninja.objects.create(
            ninja_trainee=f"{request.POST['ninja_first_name']} {request.POST['ninja_last_name']}", 
            dojo=Dojo.objects.get(id=request.POST["ninja_dojo"]))
    return redirect('/')


def delete(request):
    if request.POST["delete_type"] == "dojo":
        Dojo.objects.get(id=request.POST["delete_link"]).delete()
    else:
        Ninja.objects.get(id=request.POST["delete_link"]).delete()
    return redirect('/')
from django.shortcuts import render, redirect
from .models import Users

def index(request):
    context={
        "all_users": Users.objects.all()
    }
    return render(request, "index.html", context)

def process_user(request):
    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_entry'],
        age = request.POST['age_entry'],
    )
    return redirect("/")
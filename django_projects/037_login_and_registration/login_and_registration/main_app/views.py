from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "main_app/index.html")


def create_user(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hash_pw = bcrypt.hashpw(request.POST['new_user_password_input'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['new_user_first_name_input'],
            last_name = request.POST['new_user_last_name_input'],
            email = request.POST['new_user_email_input'],
            age = request.POST['new_user_date_input'],
            password = hash_pw
        )
        request.session['uuid'] = new_user.id
        return redirect('/landing')


def log_in_user(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST['email_input'])
        request.session['uuid'] = user.id
        return redirect('/landing')


def log_in_landing(request):
    if "uuid" not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id = request.session['uuid']),
    }
    return render(request, "main_app/landing.html", context)


def log_out(request):
    del request.session['uuid']
    return redirect("/")
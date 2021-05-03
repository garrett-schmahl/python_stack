from django.shortcuts import render, redirect
from user_control.models import User
from .models import Book


def index(request):
    if 'uuid' not in request.session:
        return redirect("/")
    context = {
        'user': User.objects.get(id = request.session['uuid']),
        'books': Book.objects.all()
    }
    return render(request, "main_app/index.html", context)


def create_book(request):  
    user = User.objects.get(id=request.session['uuid'])

    new_book = Book.objects.create(
    title = request.POST['title_input'],
    author = request.POST['author_input'],
    description = request.POST['book_description_input'],
    uploaded_by = user)

    Book.objects.get(id=new_book.id).favorite_of.add(user)
    return redirect ('/favorite_books')


def view_book(request, book_id):
    if 'uuid' not in request.session:
        return redirect("/")
    context = {
        "user":User.objects.get(id=request.session['uuid']),
        "book":Book.objects.get(id=book_id)
    }
    return render(request, 'main_app/view_book.html', context)


def like_book(request, book_id):
    user = User.objects.get(id=request.session['uuid'])
    Book.objects.get(id=book_id).favorite_of.add(user)
    return redirect ('/favorite_books')

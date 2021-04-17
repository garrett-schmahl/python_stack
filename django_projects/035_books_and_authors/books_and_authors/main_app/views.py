from django.shortcuts import render, redirect
from .models import *


def index(request, style="books"):
    if style == "books":
        pass_data = Book.objects.all()
    else:
        pass_data = Author.objects.all()

    context={
        "table_data": pass_data,
        "style": style,
    }
    return render(request,"index.html",context)


def details(request, style, id_num):
    if style == "books":
        details_data = Book.objects.get(id=id_num)
        drop_down_data = Author.objects.all()
    elif style == "authors":
        details_data = Author.objects.get(id=id_num)
        drop_down_data = Book.objects.all()

    context={
        "details_data":details_data,
        "drop_down_data":drop_down_data,
        "style": style,
    }
    return render(request,"details.html",context)


def add(request, style):
    if style == "books":
        Book.objects.create(
            title=request.POST['input_name_box'],
            description=request.POST['description_box']
        )
    else:
        Author.objects.create(
            first_name=request.POST['input_name_box'],
            last_name=request.POST['last_name'],
            notes=request.POST['description_box']
        )
    return redirect(f'/{style}')


def delete_entry(request, style):
    if style == "books":
        Book.objects.get(id=request.POST["delete_id"]).delete()
    else:
        Author.objects.get(id=request.POST["delete_id"]).delete()
    return redirect(f'/{style}')


def delete_connection(request, style, auth_id, book_id):
    if style == "books":
        Book.objects.get(id=book_id).authors.remove(Author.objects.get(id=auth_id))
        return redirect(f'/{style}/{book_id}')
    else:
        Author.objects.get(id=auth_id).books.remove(Book.objects.get(id=book_id))
        return redirect(f'/{style}/{auth_id}')


def add_connection(request, style, id_num):
    if style == "books":
        Book.objects.get(id=id_num).authors.add(Author.objects.get(id=request.POST['drop_down_select']))
    else:
        Book.objects.get(id=request.POST['drop_down_select']).authors.add(Author.objects.get(id=id_num))
    return redirect(f'/{style}/{id_num}')


def update_data(request, style, id_num):
    if style == "books":
        book_to_edit = Book.objects.get(id=id_num)
        book_to_edit.description = request.POST["description_box"]
        book_to_edit.save()
    else:
        author_to_edit = Author.objects.get(id=id_num)
        author_to_edit.notes = request.POST["description_box"]
        author_to_edit.save()
    return redirect(f'/{style}/{id_num}')


def iterate_id(request, style, id_num, direction):
    for book in Book.objects.all().order_by("id"){
        if book.id > id_num:
            smallestDiff = id_num-book.id
            smalllest
    }
    #find the closest >

    return redirect(f'/{style}/{new_id_num}')
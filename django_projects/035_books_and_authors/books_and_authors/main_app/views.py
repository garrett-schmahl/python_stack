from django.shortcuts import render, redirect
from .models import *


def index(request, page_type="books"):
    if page_type == "books":
        pass_data = Book.objects.all()
    else:
        pass_data = Author.objects.all()

    context={
        "table_data": pass_data,
        "page_type": page_type,
    }
    return render(request,"index.html",context)


def details(request, page_type, id_num):
    if page_type == "books":
        details_data = Book.objects.get(id=id_num)
        drop_down_data = Author.objects.all()
    elif page_type == "authors":
        details_data = Author.objects.get(id=id_num)
        drop_down_data = Book.objects.all()

    context={
        "details_data":details_data,
        "drop_down_data":drop_down_data,
        "page_type": page_type,
    }
    return render(request,"details.html",context)


def add(request, page_type):
    if page_type == "books":
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
    return redirect(f'/{page_type}')


def delete_entry(request, page_type):
    if page_type == "books":
        Book.objects.get(id=request.POST["delete_id"]).delete()
    else:
        Author.objects.get(id=request.POST["delete_id"]).delete()
    return redirect(f'/{page_type}')


def delete_connection(request, page_type, auth_id, book_id):
    if page_type == "books":
        Book.objects.get(id=book_id).authors.remove(Author.objects.get(id=auth_id))
        return redirect(f'/{page_type}/{book_id}')
    else:
        Author.objects.get(id=auth_id).books.remove(Book.objects.get(id=book_id))
        return redirect(f'/{page_type}/{auth_id}')


def add_connection(request, page_type, id_num):
    if page_type == "books":
        Book.objects.get(id=id_num).authors.add(Author.objects.get(id=request.POST['drop_down_select']))
    else:
        Book.objects.get(id=request.POST['drop_down_select']).authors.add(Author.objects.get(id=id_num))
    return redirect(f'/{page_type}/{id_num}')


def update_data(request, page_type, id_num):
    if page_type == "books":
        book_to_edit = Book.objects.get(id=id_num)
        book_to_edit.description = request.POST["description_box"]
        book_to_edit.save()
    else:
        author_to_edit = Author.objects.get(id=id_num)
        author_to_edit.notes = request.POST["description_box"]
        author_to_edit.save()
    return redirect(f'/{page_type}/{id_num}')


def next_item(request, page_type, id_num, direction):
    trigger=False
    new_id_num = False
    if direction == "next":
        for book in Book.objects.all():
            if trigger == True:
                new_id_num= book.id
                break
            if book.id == id_num:
                trigger=True
        if new_id_num:
            return redirect(f'/{page_type}/{new_id_num}')
        else:
            return redirect(f'/{page_type}/{id_num}')
            
    else:
        for book in Book.objects.all()[::-1]:
            if trigger == True:
                new_id_num = book.id
                break
            if book.id == id_num:
                trigger=True
        if new_id_num:
            return redirect(f'/{page_type}/{new_id_num}')
        else:
            return redirect(f'/{page_type}/{id_num}')

    
 
        
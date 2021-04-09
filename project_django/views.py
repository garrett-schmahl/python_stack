from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
  return redirect("/blogs")

def index(request):
  return HttpResponse("placeholder to display a list of blogs")  

def new(request):
  return HttpResponse("placeholder to display a create new form")  

def create(request):
  return redirect("/")

def show(request, number):
  return HttpResponse(f"placeholder to later display blog number: {number}")

def edit(request, number):
  return HttpResponse(f"placeholder to edit blog: {number}")

def destroy(request, number):
  return redirect("blogs")

def info(request):
  return JsonResponse({"response": "JSON response from redirected_method", "status": True})

# def weeb_stuff(request):
#     return HttpResponse("sasuke-sama daisuke")  

# def welp(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})
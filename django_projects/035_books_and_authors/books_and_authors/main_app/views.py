from django.shortcuts import render, HttpResponse

def index(response):
    return HttpResponse("hola senior")

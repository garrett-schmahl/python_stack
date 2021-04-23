from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create_book),
    path('<int:book_id>/view', views.view_book),
    path('<int:book_id>/like', views.like_book),
]
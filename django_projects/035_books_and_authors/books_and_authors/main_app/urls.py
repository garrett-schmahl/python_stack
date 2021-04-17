from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<style>/<int:auth_id>/<int:book_id>/disconnect', views.delete_connection),
    path('<style>/<int:id_num>/update', views.update_data),
    path('<style>/<int:id_num>/connect', views.add_connection),
    path('<style>/delete', views.delete_entry),
    path('<style>/add', views.add),
    path('<style>/<int:id_num>', views.details),
    path('<style>', views.index),
]
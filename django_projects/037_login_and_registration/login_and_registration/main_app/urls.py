from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user/create', views.create_user),
    path('user/login', views.log_in_user),
    path('landing', views.log_in_landing),
    path('user/logout', views.log_out),
]
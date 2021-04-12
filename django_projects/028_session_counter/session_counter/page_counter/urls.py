from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('add_two', views.add_two),
    path('add_value', views.add_value),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('shows', views.all_shows_render),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>', views.show_detail),
    path('shows/<int:show_id>/destroy', views.delete_show),
]
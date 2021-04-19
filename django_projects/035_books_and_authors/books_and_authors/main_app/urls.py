from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<page_type>/<int:auth_id>/<int:book_id>/disconnect', views.delete_connection),
    path('<page_type>/<int:id_num>/update', views.update_data),
    path('<page_type>/<int:id_num>/connect', views.add_connection),
    path('<page_type>/<int:id_num>/<direction>', views.next_item),
    path('<page_type>/delete', views.delete_entry),
    path('<page_type>/add', views.add),
    path('<page_type>/<int:id_num>', views.details),
    path('<page_type>', views.index),
]
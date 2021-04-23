from django.db import models
from user_control.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='uploaded_books', on_delete= models.SET_NULL, null=True)
    favorite_of = models.ManyToManyField(User, related_name="favorite_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
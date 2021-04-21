from django.db import models
import bcrypt
from datetime import datetime
import re



class User_Manager(models.Manager):
    def registration_validator(self, post_data):
        errors = {}

        if len(post_data['new_user_first_name_input']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(post_data['new_user_last_name_input']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."

        user_list = User.objects.filter(email = post_data['new_user_email_input'])

        if len(user_list) > 0:
            errors['email'] = "Email is already in use."
        
        if len(post_data['new_user_password_input']) < 4:
            errors['password'] = "Password must be at least 4 characters."
        if post_data['new_user_password_input'] != post_data['new_user_password_check']:
            errors['password_check'] = "Password does not match."

        if len(post_data['new_user_date_input']) < 1:
            errors['date'] = "You must enter a birth date."
        else:
            form_date = datetime.strptime(post_data['new_user_date_input'], "%Y-%m-%d")
            if datetime.now() < form_date:
                errors["date"] = "Are you a terminator?"
            elif datetime.now().year - form_date.year < 13:
                errors["date"] = "You must be at least 13."
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    age=models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = User_Manager()
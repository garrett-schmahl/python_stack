from django.db import models
from datetime import datetime
import time

class ShowManager(models.Manager):
    def validator(self, post_data, shows):
        errors = {}
        for show in shows:
            if post_data['show_name_input'] == show.name:
                errors['exists'] = "A show with that name already exists"
        if len(post_data['show_name_input']) < 1:
            errors['length'] = "Name must be at least 2 letters"
        if post_data['show_description'] != "":
            if len(post_data['show_description']) < 10:
                errors['length'] = "Description must be at least 10 letters"
        now = datetime.now()
        release_date = time.strptime(post_data['show_date_input'], "%Y-%m-%d")
        if release_date.tm_year < now.year:
            pass
        elif release_date.tm_year == now.year:
            if release_date.tm_mon < now.month:
                pass
            elif release_date.tm_mon == now.month:
                if release_date.tm_mday <= now.day:
                    pass
                else:
                    errors['date']= "That date is in the future."
        return errors


class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Show(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    network = models.ForeignKey(Network, related_name="shows", on_delete= models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

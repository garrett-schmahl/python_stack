from django.db import models

class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['name'] < 1):
            errors['length'] = "name must be at east 1 letter"
        return errors


class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Show(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    network = models.ForeignKey(Network, related_name="shows", on_delete= models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
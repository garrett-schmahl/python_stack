from django.db import models

class Dojo(models.Model):
    dojo_name = models.CharField(max_length=255)
    dojo_city = models.CharField(max_length=255)
    dojo_state = models.CharField(max_length=255)
    desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    ninja_trainee = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


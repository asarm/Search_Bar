from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)
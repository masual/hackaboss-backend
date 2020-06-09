from django.db import models

# Create your models here.

class Compose(models.Model):
    name = models.CharField(max_length=32, unique=True)
    yaml = models.TextField(null=False, blank=False)
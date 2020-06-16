from django.db import models


# Create your models here.
class HelloWorld(models.Model):
    hello_world = models.CharField(max_length=100, default=None)

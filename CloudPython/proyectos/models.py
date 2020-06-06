from django.db import models
from usuarios.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    made = models.DateTimeField(auto_now_add = True)
    upload = models.DateTimeField(auto_now = True)
    image = models.ImageField(default = 'null', upload_to = "Categories")


class Proyect(models.Model):
    name = models.CharField(max_length=50)
    goal = models.FloatField()
    actual = models.FloatField()
    deadline = models.DateTimeField(auto_now_add=False)
    description = models.CharField(max_length=1500)
    image = models.ImageField(default = 'null', upload_to = "Proyects")
    made = models.DateTimeField(auto_now_add = True)
    upload = models.DateTimeField(auto_now = True)
    category = models.ForeignKey("Category", verbose_name=("Category"), on_delete=models.CASCADE)
    userOwner = models.ForeignKey(User, verbose_name=("Owner"), related_name='Owner',on_delete=models.CASCADE)
    usersPatrons = models.ManyToManyField(User, verbose_name=("Patrons"))




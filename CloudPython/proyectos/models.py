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
    deadline = models.DateField(auto_now_add=False)
    description = models.CharField(max_length=1500)
    image = models.ImageField(default = 'null', upload_to = "Proyects")
    made = models.DateTimeField(auto_now_add = True)
    upload = models.DateTimeField(auto_now = True)
    category = models.ForeignKey("Category", verbose_name=("Category"), on_delete=models.CASCADE)
    userOwner = models.ForeignKey(User, verbose_name=("Owner"), related_name='Owner',on_delete=models.CASCADE)
    Patrons = models.ManyToManyField(User,
        through = 'Patron',
        through_fields = ('proyecto','patron'),
        verbose_name=("Patrons"),
        default = 'null')

class Patron(models.Model):
    proyecto  = models.ForeignKey(Proyect, verbose_name = ("Proyecto"), on_delete=models.CASCADE)
    patron = models.ForeignKey(User, verbose_name = ("Patron"), on_delete=models.CASCADE)
    money = models.FloatField(default = 0)
    date = models.DateTimeField(default = datetime.now())

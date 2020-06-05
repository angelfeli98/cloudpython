from django.db import models

# Create your models here.

class User(models.Model):

    user = models.CharField(max_length=50)
    name = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    made = models.DateTimeField(auto_now_add = True)
    upload = models.DateTimeField(auto_now = True)
    photo = models.ImageField(default = 'null', upload_to = "users")
    wallet = models.FloatField()

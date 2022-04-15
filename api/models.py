from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=25)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=250)
    level1 = models.IntegerField(default=0)
    level2 = models.IntegerField(default=0)
    level3 = models.IntegerField(default=0)
    api_key = models.TextField(max_length=250)


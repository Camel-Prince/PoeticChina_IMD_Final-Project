from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField('username', max_length=100, default="Null", primary_key=True)
    password = models.CharField('password', max_length=100, default="Null")

    class Meta:
        db_table = 'users'


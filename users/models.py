from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class Users(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=50, verbose_name='Familiya')
    username = models.CharField(max_length=50, verbose_name='Foydalanuvchi nomi', unique=True)
    email = models.EmailField(max_length=50, verbose_name='Email')
    password1 = models.CharField(max_length=50, verbose_name='Parol')
    password2 = models.CharField(max_length=50, verbose_name='Parolni takrorlang')

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    is_anonymous = False
    is_authenticated = True


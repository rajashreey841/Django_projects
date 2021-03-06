from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=225,unique=True)
    phone=models.CharField(null=True,max_length=255)
    #REQUIRED_FIELDS=['username','phone','first_name','last_name']
    REQUIRED_FIELDS=['username','phone',]
    USERNAME_FIELD='email'
    def get_username(self):
        return self.email
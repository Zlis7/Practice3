from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(upload_to = "photo/%Y/%m/%d/", 
        blank = True, verbose_name = "Фотография")
    date_birth = models.DateTimeField(blank = False, null = False,
        verbose_name = "Дата рождения")
 

class UploadFiles(models.Model):
    photo = models.ImageField(upload_to='uploads_model')
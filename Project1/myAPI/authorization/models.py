from django.db import models
from django.urls import reverse

class Authorization(models.Model):
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add = True, verbose_name='Дата создания')
    is_delete = models.BooleanField(default=False, verbose_name='Был удалён')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    #photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    #slug = models.SlugField(max_lenght=255, unique = True, db_index = True, verbose_name='NAMEEEEE')


    def __str__(self):
        return self.login
    
    def get_absolute_url(self):
        return reverse('registrationID', kwargs={'id': self.pk})
    
    class Meta: #Для админ панели
        verbose_name = 'Зарегистрированные пользователи'
        verbose_name_plural = 'Зарегистрированные пользователи'
        ordering = ['-date_creation']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')


    class Meta: #Для админ панели
        verbose_name = 'Категории (просто чтобы были)'
        verbose_name_plural = 'Категории (просто чтобы были)'
        ordering = ['id']

    def __str__(self):
        return self.name 
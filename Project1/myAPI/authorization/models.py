from django.db import models
from django.urls import reverse

class Authorization(models.Model):
    login = models.CharField(max_length=15, verbose_name = 'Логин', unique =  True)
    password = models.CharField(max_length=20, verbose_name = 'Пароль')
    date_creation = models.DateTimeField(auto_now_add = True, verbose_name='Дата создания')
    is_delete = models.BooleanField(default=False, verbose_name='Был удалён')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank = True, verbose_name = 'Категория')

    photo = models.ImageField(upload_to= 'images/', null=True)
    slug = models.SlugField(max_length=255, unique = True, db_index = True, verbose_name='NAMEEEEE', null=True)


    def __str__(self):
        return self.login
    
    def get_absolute_url(self):
        return reverse('registrationID', kwargs={'id': self.pk})
        #return reverse('registrationID', kwargs={'slug': self.slug})
    
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
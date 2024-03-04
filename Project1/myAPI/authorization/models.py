from django.db import models


class Authorization(models.Model):
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add = True)
    is_delete = models.BooleanField(default=False) 

    def __str__(self):
        return self.login
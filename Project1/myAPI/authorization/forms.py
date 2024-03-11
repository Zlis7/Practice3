from django import forms
from .models import *

# Форма не связанная с БД
#class addNewUser(forms.Form):
#    login = forms.SlugField(max_length=15, label='Логин')
#    password = forms.CharField(max_length=20, label='Пароль', empty_label = "Не задано")

class addNewUser(forms.ModelForm):
    
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs )
        self.fields['cat'].empty_label = 'Не дано'
    
    class Meta:
        model = Authorization
        #fields = '__all__'
        fields = ['login', 'password', 'cat']
        widget = {
            'login': forms.TextInput(attrs = {'class' : 'form-input'}),
            'password': forms.TextInput(attrs = {'class' : 'form-input'})
        }
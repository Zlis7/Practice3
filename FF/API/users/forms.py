from django import forms
from django.contrib.auth import get_user_model

class LoginUser(forms.Form):
    username = forms.CharField(label='Логин', max_length=20)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class RegisterUser(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=20)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['photo','username', 'email', 'first_name', 'last_name', 'date_birth', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя', 
            'last_name': 'Фамилия'
        }
    
    
    
    def clean_password2(self):
        form_data = self.cleaned_data
        
        if form_data['password'] != form_data['password2']:
            raise forms.ValidationError('Пороли не сопадают')
        
        return form_data['password']
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if get_user_model().objects.filter(email = email).exists():
            raise forms.ValidationError('Такой email уже существует')
        
        return email


class UploadImageForm(forms.Form):
    photo = forms.ImageField(label='Фото')
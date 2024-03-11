from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('allusers/', views.all_users, name='allUsers'),
    path('media/', views.media_download, name='media')
]

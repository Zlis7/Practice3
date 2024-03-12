from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('user/<int:id>', views.user_id, name='userID'),
    path('media/', views.media_download, name='media')
]

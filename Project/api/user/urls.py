from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'user'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/',views.register, name='register'),
    path('fileupload/',views.fileupload, name='fileupload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
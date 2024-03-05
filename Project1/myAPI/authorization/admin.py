from django.contrib import admin
from .models import *

@admin.register(Authorization)
class AuthorizationAdmin(admin.ModelAdmin):
    list_display = ('id','login','password', 'date_creation', 'is_delete')
    list_display_links = ('id','login')
    search_fields = ('id','login')
    list_editable = ('is_delete',)
    list_filter = ('is_delete','date_creation')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#admin.site.register(Authorization, AuthorizationAdmin)
#admin.site.register(Category, CategoryAdmin)
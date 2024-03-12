from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)


#@admin.register(User)
#class Admin(admin.ModelAdmin):
#    list_display = ('post_photo' , 'first_name', 'last_name', 'email')
#    readonly_fields = ['post_photo']
#
#    @admin.display(description = 'Вид фото')
#   def post_photo(self, user:User):
#        if user.photo:
#            return mark_safe(f"<img src='{user.photo.url}' width=50px />")
#        return "Без фото"

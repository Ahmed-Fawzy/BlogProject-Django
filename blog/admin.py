from django.contrib import admin

from .models import User, Permission, Post

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
    search_fields = ['user_name']
    filter_horizontal = ('permission',)

admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.register(Post)



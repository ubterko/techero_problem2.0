from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models
# Register your models here.
class UserAdmin(BaseUserAdmin):
        ordering = ['id']
        list_display = ['email','name']
        fieldsets = (
            (None,{'fields':('email',)}),
            (_('Personal Info'),{'fields':('name',)}),
            (_('Permissions'),{'fields':('is_proprietor','is_staff','is_superuser')}),
        )
        add_fieldsets = (
            (None,
            {'classes':('wide',),
            'fields':('email', 'password1','password2','is_proprietor')}),
        )

admin.site.register(models.User, UserAdmin)

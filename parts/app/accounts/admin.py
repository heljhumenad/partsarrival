from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# change this to avoid direct calling from main config
from parts.config.settings import base

# Register model
from .models import CustomUser
from parts.app.forms import auth_forms

admin.site.site_header = base.ADMIN_SITE_HEADER
admin.site.site_title = base.ADMIN_SITE_TITLE
admin.site.index_title = base.ADMIN_SITE_TITLE

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model
    add_form = auth_forms.CustomUserCreationForm
    form = auth_forms.CustomUserChangeForm
    list_display = [
                    'first_name', 'last_name',
                    'email', 'username',
                   ]


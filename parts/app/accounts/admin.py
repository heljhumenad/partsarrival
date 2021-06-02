from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register model
from parts.app.accounts.models import CustomUser, ProfileUser
from parts.app.accounts import forms
# change this to avoid direct calling from main config

# Config settings for Look and feel
ADMIN_SITE_HEADER = 'PAS System'
ADMIN_INDEX_TITLE = 'PARTS ARRIVAL SYSTEM'
ADMIN_SITE_TITLE = 'PAS ARRIVAL SYSTEM'


admin.site.site_header = ADMIN_SITE_HEADER
admin.site.site_title = ADMIN_SITE_TITLE
admin.site.index_title = ADMIN_INDEX_TITLE


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = get_user_model
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    list_display = [
        'first_name', 'last_name',
        'email', 'username',
    ]

@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    model = ProfileUser
    list_display = ["user", "role"]


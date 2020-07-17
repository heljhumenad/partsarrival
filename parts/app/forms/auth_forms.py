from django.contrib.auth import forms

from parts.app.accounts.models import CustomUser


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = CustomUser
        fields = forms.UserCreationForm.Meta.fields


class CustomUserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'first_name', 'last_name', 'email']
        exclude = ['password']


class AccountPasswordResetForm(forms.PasswordResetForm):
    class Meta(forms.PasswordResetForm):
        model = CustomUser


class AccountPasswordChangeForm(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        model = CustomUser


class AccountSetPasswordForm(forms.SetPasswordForm):
    class Meta(forms.SetPasswordForm):
        model = CustomUser

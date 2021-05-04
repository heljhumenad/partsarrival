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
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            self.fields["username"].widget.attrs["readonly"] = True


class AccountPasswordResetForm(forms.PasswordResetForm):
    class Meta(forms.PasswordResetForm):
        model = CustomUser


class AccountPasswordChangeForm(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        model = CustomUser


class AccountSetPasswordForm(forms.SetPasswordForm):
    class Meta(forms.SetPasswordForm):
        model = CustomUser

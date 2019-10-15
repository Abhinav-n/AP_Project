from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class GuestForm(forms.Form):
    email = forms.EmailField(required=True)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(UserRegisterForm, self).save(commit=False)
            user.email = clean_data['email']

            if commit:
                user.save()
            return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        def save(self, commit=True):
            user = super(UserRegisterForm, self).save(commit=False)
            user.first_name = clean_data['first_name']
            user.last_name = clean_data['last_name']

            if commit:
                user.save()
            return user

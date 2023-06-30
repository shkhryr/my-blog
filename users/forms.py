from django.contrib.auth.models import User
from .models import Profile
from django import forms


class CreateProfile(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

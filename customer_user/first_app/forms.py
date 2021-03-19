from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomerForm(forms.ModelForm):

    class Meta():
        model = CustomUser
        fields = ('email','fullname','street','city','pincode','mobile','password')
        widgets = {
            'password': forms.PasswordInput(),
        }
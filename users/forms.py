from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Users


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ismingizni kiriting...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Familiyangizni kiriting...'}),
            'username': forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Foydalanuvchi nomini kiriting...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Emailingizni kiriting...'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Parolni kiriting...'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Parolni takrorlang...'}),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Foydalanuvchi nomini kiriting...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                 'placeholder': 'Foydalanuvchi parolini kiriting...'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control py-4',
                                                 'placeholder': 'Ismingizni kiriting...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control py-4',
                                                'placeholder': 'Familiyangizni kiriting...'}),
            'image': forms.FileInput(attrs={'class': 'form-control py-1',
                                            'placeholder': 'Rasm kiriting...'}),
        }

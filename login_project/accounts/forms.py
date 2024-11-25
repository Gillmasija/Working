# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Signup form with password confirmation
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email field, make it required

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Customizing password validation and display
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        return password2


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

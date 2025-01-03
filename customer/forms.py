from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'})
    )
    locality = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Locality', 'class': 'form-control'})
    )
    city = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'})
    )
    zipcode = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=Customer.STATE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create and save the Customer object
            Customer.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                locality=self.cleaned_data['locality'],
                city=self.cleaned_data['city'],
                zipcode=self.cleaned_data['zipcode'],
                state=self.cleaned_data['state']
            )
        return user



class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your password',
        }),
    )

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'autofocus': True,
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your old password',
        }),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your new password',
        }),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Confirm your new password',
        }),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your email',
        }),
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'autofocus': True,
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Enter your new password',
        }),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black focus:border-black',
            'placeholder': 'Confirm your new password',
        }),
    )

    field_order = ['new_password1', 'new_password2']
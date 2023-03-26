from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not User.objects.filter(email__iexact=email, is_active=True).exists():
#             raise forms.ValidationError("This email address is not associated with any active account.")
#         return email
    
#change password form
class Password_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class HotelApplicationForm(ModelForm):
    class Meta:
        model = HotelApplication
        fields = '__all__'
        exclude = ['hotel_status']
        # widgets = {
        #     'hotel_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'hotel_address': forms.TextInput(attrs={'class': 'form-control'}),
        #     'hotel_contact': forms.TextInput(attrs={'class': 'form-control'}),
        #     'hotel_email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'hotel_description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'hotel_image': forms.FileInput(attrs={'class': 'form-control'}),
        # }
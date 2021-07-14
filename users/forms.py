from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUsers


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUsers
        fields = ('username', 'email', 'age', 'phone_number',) 
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'age', 'phone_number',)
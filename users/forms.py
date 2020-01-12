from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from Blog_sys.models import Post , Messages
from crispy_forms.layout import Field

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title' , 'content' , 'technology' , 'policy' , 'sport' , 'jobs' , 'cars' , 'services', 'culture' , 'animals']

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']
                 
    
        
        
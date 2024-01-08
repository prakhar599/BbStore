from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Author


class signUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name')

class logInForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['profile_pic', 'bio', 'tagline', 'twitter_profile', 'instagram_profile', 'github', 'stackoverflow', 'personal_website', 'linkedin_channel']

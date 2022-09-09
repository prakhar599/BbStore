from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class signUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name')
        
class logInForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name')        



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

   


from django import forms
from .models import Picture
  
class PictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = [ "name", "tags","picture_Main_Img", "is_visible", "user"]
        


class UpdatePictureForm(forms.ModelForm):

    class Meta:
        model = Picture
        fields = [ "name", "tags","picture_Main_Img", "is_visible"]



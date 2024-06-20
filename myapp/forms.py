from django import forms 
from . models import LoginTable,UserProfile

class UserProileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LoginTableForm(forms.ModelForm):
    class Meta:
        model = LoginTable
        fields = '__all__'
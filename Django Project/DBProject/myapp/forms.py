from django import forms
from .models import userinfo

class userinfoForm(forms.ModelForm):
    class Meta:
        model=userinfo
        fields='__all__'



class updateinfo(forms.ModelForm):
    class Meta:
        model=userinfo
        fields=['name','email','dob','mobile','address']
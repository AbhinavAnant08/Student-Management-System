from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Students

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password1= forms.CharField(max_length=50, label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(max_length=50, label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class meta():
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class addRecord(forms.ModelForm):
    std_name = forms.CharField(required=True,label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    std_id = forms.IntegerField(required=True,label="", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Id'}))
    std_course = forms.CharField(required=True,label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Course'}))
    std_Phone_no = forms.CharField(required=True,label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone no'}))
    std_class = forms.CharField(required=True,label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Class'}))

    class Meta:
        model = Students
        fields = ("std_name","std_id", "std_course","std_Phone_no","std_class")

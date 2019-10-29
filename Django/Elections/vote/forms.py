from django import forms
from django.contrib.auth.models import User


gender = (
	('male','Male'),
	('female','Female'),
	('others','others')
	)
bloodGroup = (
	('A+','A+'),
	('A-','A-'),
	('B+','B+'),
	('B-','B-'),
	('O+','O+'),
	('O-', 'O-'),
	('AB+','AB+'),
	('AB-','AB-')
	)
class CustomForms(forms.Form):
	userName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username' }), label='')


class RegisterForm(forms.Form):
	username = forms.CharField(label='Username:', max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username' }))
	password1 = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
	password2 = forms.CharField(label='Re-Password', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Re-Password'}))
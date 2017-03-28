from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget 


class LoginForm(forms.Form):
	username =forms.CharField(max_length=30)
	password=forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		username = self.cleaned_data.get('username')
		password= self.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Not valid user")
		return self.cleaned_data

class RegistrationForm(forms.Form):
	username =forms.CharField(max_length=30)
	password=forms.CharField(widget=forms.PasswordInput())
	email=forms.CharField(widget=forms.EmailInput())
	
	def clean(self):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		if User.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('user already exist')
		return self.cleaned_data

class EditForm(forms.Form):
	author=forms.CharField(max_length=30)
	title=forms.CharField(max_length=200)
	text=forms.CharField(max_length=1000)
	published_date=forms.DateTimeField(widget = forms.SelectDateWidget)
	image=forms.ImageField()
	
	def clean(self):
		author=self.cleaned_data.get('author')
		title=self.cleaned_data.get('title')
		text=self.cleaned_data.get('text')
		published_date=self.cleaned_data.get('published_date')
		image=self.cleaned_data.get('image')
		
		
		
		
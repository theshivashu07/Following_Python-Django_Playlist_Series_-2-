
from django import forms

class userForm(forms.Form):
	# firstvalue=forms.CharField(label="First Value", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
	# secondvalue=forms.CharField(label="First Value", required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
	firstvalue=forms.CharField(label="First Value", widget=forms.TextInput(attrs={'class':"form-control"}))
	secondvalue=forms.CharField(label="First Value", widget=forms.TextInput(attrs={'class':"form-control"}))
	# email=forms.EmailField()














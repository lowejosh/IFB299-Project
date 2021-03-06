# Imports
from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from sprint1.models import EmailForm, PostImage

from sprint1.models import Review
from .models import Bug, EmailForm, Review, LocationSuggestion, Subscription


# Sign up form (additional) fields
class SignUpForm(UserCreationForm):
    firstName = forms.CharField(label='First Name', required=True)   # Note for later: help_text can be an additional parameter
    lastName = forms.CharField(label='Last Name', required=True)
    gender = forms.ChoiceField(choices=[(1, "Male"), (2, "Female"), (3, "Other")])
    accountType = forms.ChoiceField(label='Account Type', choices=[(1, "Student"), (2, "Business"), (3, "Tourist")])
    dateOfBirth = forms.DateField(label='Date of Birth', required=True, widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyy'}))
    email = forms.EmailField(label='Email Address', required=True, widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    phoneNumber = forms.RegexField(label='Phone Number', regex=r'^\+?1?\d{9,15}$', required=False)
    address = forms.CharField(label='Home Address', required=True)

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'gender', 'accountType', 'email', 'dateOfBirth', 'phoneNumber', 'address', 'password1', 'password2')

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password',)

class DeleteUserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Username'}))

class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'Recipient Email Address'}))

    class Meta:
        model = EmailForm
        fields = ('email')

class ContactForm(forms.Form):
	from_email = forms.EmailField()
	subject = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)
	sendto_email = forms.EmailField()

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'reviewText']
        labels = {'reviewText': 'Review', 'rating': 'Rating'}

class PostImage(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = {
            "title",
            "content",
            "image",
        }

class BugForm(forms.Form):
    subject = forms.ChoiceField(label = 'Subject', choices = [('A', 'Security'), ('B', 'Visual Bug'), ('C', 'Feature Not Working'), ('D', 'Website Crashing'), ('E', 'Other')])
    description = forms.CharField(label = 'Description', widget=forms.Textarea, max_length = 300)

    class Meta:
        model = Bug
        field = ['subject', 'description']
        labels = {'subject' : 'Subject:', 'description' : 'Description'}

# Suggest Location form
class SuggestLocationForm(ModelForm):
    class Meta:
        model = LocationSuggestion
        fields = ['locationName', 'locationBio', 'locationAddress', 'locationType', 'latitude', 'longitude']
        labels = {'locationName': 'Location Name', 'locationBio': 'Location Bio', 'locationAddress': 'Location Address', 'locationType' : 'Location Type',}

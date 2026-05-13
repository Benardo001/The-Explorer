from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Beach, Booking, Review


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class BeachForm(forms.ModelForm):
    class Meta:
        model = Beach
        fields = [
            'name',
            'location',
            'description',
            'activities',
            'price',
            'image',
            'latitude',
            'longitude',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'activities': forms.Textarea(attrs={'rows': 3}),
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'check_in',
            'check_out',
            'guests',
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'comment',
        ]
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

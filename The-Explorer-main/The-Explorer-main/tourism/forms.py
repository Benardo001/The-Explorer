from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Beach, Booking, Review, TouristAttraction, Accommodation, Transport, ContactMessage, Feedback


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


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-control-custom', 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com', 'class': 'form-control-custom', 'id': 'id_email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control-custom', 'id': 'id_subject'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'form-control-custom', 'id': 'id_message'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'rating',
            'comment',
        ]
        widgets = {
            'rating': forms.HiddenInput(attrs={'id': 'id_rating'}),
            'comment': forms.Textarea(attrs={'rows': 5, 'class': 'form-control-custom', 'id': 'id_comment'}),
        }


class AttractionForm(forms.ModelForm):
    class Meta:
        model = TouristAttraction
        fields = [
            'name',
            'location',
            'category',
            'description',
            'entry_fee',
            'best_time_to_visit',
            'image',
            'latitude',
            'longitude',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'best_time_to_visit': forms.TextInput(attrs={'placeholder': 'e.g., June - October'}),
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
        }


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = [
            'name',
            'location',
            'accommodation_type',
            'description',
            'price_per_night',
            'max_guests',
            'amenities',
            'image',
            'latitude',
            'longitude',
            'contact_info',
            'website',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'amenities': forms.TextInput(attrs={'placeholder': 'e.g., WiFi, Pool, Restaurant'}),
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Phone or email'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = [
            'name',
            'transport_type',
            'description',
            'location',
            'destination',
            'price_per_trip',
            'price_unit',
            'capacity',
            'amenities',
            'image',
            'contact_info',
            'website',
            'latitude',
            'longitude',
            'available_24_7',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'amenities': forms.TextInput(attrs={'placeholder': 'e.g., AC, WiFi, Luggage space'}),
            'latitude': forms.NumberInput(attrs={'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'step': 'any'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Phone or email'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
            'price_unit': forms.TextInput(attrs={'placeholder': 'e.g., trip, hour, day'}),
        }

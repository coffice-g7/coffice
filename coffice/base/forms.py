from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.utils import timezone


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['cafe', 'date', 'num_people', 'duration']
        widgets = {
            'cafe': forms.HiddenInput(),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'num_people': forms.NumberInput(attrs={'min': 1}),
            'duration': forms.NumberInput(attrs={'min': 0}),
        }
        
    def clean_date(self):
        date = self.cleaned_data['date']
        current_datetime = timezone.now()
        if date <= current_datetime:
            raise forms.ValidationError("Reservation date should be in the future.")
        return date
        
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

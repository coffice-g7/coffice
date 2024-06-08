from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.utils import timezone
from .models import Cliente


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
        
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Nome de usuário")
    cpf = forms.CharField(max_length=14, required=True, label="CPF")
    email = forms.EmailField(required=True, label="E-mail")
    cep = forms.CharField(max_length=9, required=True, label="CEP")
    number = forms.CharField(max_length=10, required=True, label="N*")

    class Meta:
        model = User
        fields = ("username", "first_name", "cpf", "email", "password1", "password2", "cep", "number")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            cpf = self.cleaned_data["cpf"]
            cep = self.cleaned_data["cep"]
            number = self.cleaned_data["number"]
            Cliente.objects.create(user=user, cpf=cpf, cep=cep, number=number)
        return user
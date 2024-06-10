from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Cliente
from django.core.exceptions import ValidationError


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(self.request, username=User.objects.filter(email=email).first(), password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Email ou senha inválidos.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
     
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
        if date < timezone.now():
            raise ValidationError("Essa data já passou.")
        return date
        
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
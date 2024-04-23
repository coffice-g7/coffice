from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import Cliente

from .models import coffee_shop

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            cpf = request.POST.get('cpf')
            phone_number = request.POST.get('phone_number')
            client_new = Cliente(user=user, phone_number=phone_number, cpf=cpf)
            try:
               client_new.save()
            except Exception as e:
               print("Erro ao salvar cliente:", e)
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm(request.POST)
    return render(request, 'signup.html', {'form': form})


def home(request):
    # Recebe o usuário logado
    user = request.user
    
    # Inicializa o array de coffee shops que vai para a home
    coffee_shops = []
    
    # Busca todas as instâncias de coffee shops
    for coffee_shop_obj in coffee_shop.objects.all():
        # Monta o payload de dados do coffee shop para a home
        coffee_shop_data = {
            'name': coffee_shop_obj.name,
            'description': coffee_shop_obj.description,
            'reservation_cost': coffee_shop_obj.reservation_cost,
            'coffee_spotlight': coffee_shop_obj.coffee_spotlight,
            'internet_speed': coffee_shop_obj.internet_speed,
            'vegan_options': coffee_shop_obj.vegan_options,
            'zero_lactose_options': coffee_shop_obj.zero_lactose_options,
            'gluten_free_options': coffee_shop_obj.gluten_free_options,
            'accessibility': coffee_shop_obj.accessibility,
            'has_parking': coffee_shop_obj.has_parking,
            'street': coffee_shop_obj.street,
            'number': coffee_shop_obj.number,
            'neighborhood': coffee_shop_obj.neighborhood,
        }
        
        # Adiciona o coffee shop ao array de coffee shops
        coffee_shops.append(coffee_shop_data)
    
    # Monta o contexto da home
    context = {
        'coffee_shops': coffee_shops,
        'user': user
    }
    
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')

def logout(request):
    auth_logout(request)
    return redirect('home')
    


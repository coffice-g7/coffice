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
from django.views.generic import DetailView
from django.utils import timezone

from .forms import CustomUserCreationForm
from .forms import ReservationForm
from .models import Reservation
from .models import Cliente
from .models import coffee_shop, Favorite

# Create your views here.

@login_required
def make_reservation(request, cnpj):
    cafe = get_object_or_404(coffee_shop, cnpj=cnpj)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(initial={'cafe': cafe})
    return render(request, 'make_reservation.html', {'form': form, 'cafe': cafe})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    current_datetime = timezone.now()
    for res in reservations:
        if res.date < current_datetime:
            res.delete()
    return render(request, 'reservation_list.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id, user=request.user)
    if reservation.status == 'P':
        reservation.status = 'X'
        reservation.save()
    return redirect('reservation_list')

def login_view(request):
    error_message = None
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
                error_message = "Credenciais inválidas. Tente novamente."
        else:
            error_message = "Por favor, corrija os erros no formulário."        
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error_message})

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
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user_id=user.id)
    
    # Inicializa o array de coffee shops que vai para a home
    coffee_shops = []
    
    # Busca todas as instâncias de coffee shops
    for coffee_shop_obj in coffee_shop.objects.all():
        # Verifica se o coffee shop está nos favoritos do usuário
        is_favorited = favorites.filter(coffee=coffee_shop_obj, user_id=user.id).exists()
        
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
            'cnpj': coffee_shop_obj.cnpj,
            'favorited': is_favorited,
        }
        
        # Adiciona o coffee shop ao array de coffee shops
        coffee_shops.append(coffee_shop_data)
    
    # Ordena as babás pelo atributo favorited
    coffee_shops.sort(key=lambda x: x['favorited'], reverse=True)

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

def coffee_shop_detail(request, pk):
    coffee_shop_obj = get_object_or_404(coffee_shop, pk=pk)
    return render(request, 'coffee_shop_detail.html', {'coffee_shop': coffee_shop_obj})

def favorited_coffee_shop(request, pk):
    user = request.user

    if request.method == 'POST':
        coffee = coffee_shop.objects.get(cnpj=pk)
        
        favorited = {}
        
        try:
            favorited = Favorite.objects.get(user=user, coffee=pk) 
            Favorite.delete(favorited)
        except:
            Favorite.objects.create(user=user, coffee=coffee)

        redirect_to = request.POST.get('redirect_to', 'home')

    return redirect(redirect_to)

def myprofile(request):
    user = request.user
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user=user)

    coffee_shops = []
    
    # Inicializa o array de coffee shops favoritadas
    for favorite in favorites:
        coffee_shop_obj = favorite.coffee
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
            'cnpj': coffee_shop_obj.cnpj,
            'favorited': True,  # Define como favorited
        }
        coffee_shops.append(coffee_shop_data)
    
    # Monta o contexto da página de perfil
    context = {
        'coffee_shops': coffee_shops,
        'user': user
    }

    return render(request, 'myprofile.html', context)


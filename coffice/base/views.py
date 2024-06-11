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
from .forms import CustomUserCreationForm, EmailAuthenticationForm

from .forms import CustomUserCreationForm
from .forms import ReservationForm
from .models import Reservation
from .models import Cliente
from .models import coffee_shop, Favorite
from .models import Review
from .forms import ReviewForm

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
            messages.success(request, 'Reserva realizada com sucesso!')
            return redirect('myprofile')
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = ReservationForm(initial={'cafe': cafe})
    return render(request, 'make_reservation.html', {'form': form, 'cafe': cafe})

@login_required
def reservation_list(request):
    current_datetime = timezone.now()
    # Filtrar e deletar reservas antigas
    Reservation.objects.filter(user=request.user, date__lt=current_datetime).delete()
    # Obter todas as reservas atualizadas
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
        if reservation.status == 'P':
            reservation.status = 'X'
            reservation.save()
            messages.success(request, 'Reserva cancelada com sucesso.')
    except Reservation.DoesNotExist:
        messages.error(request, 'Reserva não encontrada ou já cancelada.')
    return redirect('myprofile')

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            error_message = "Email ou senha inválidos."
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error_message})

def register_view(request):
    error_message = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  
            return redirect('home')  
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()
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
            'alone': coffee_shop_obj.alone,
            'has_meeting_room': coffee_shop_obj.has_meeting_room,
            'has_silent_environment': coffee_shop_obj.has_silent_environment,
            'allow_reservation': coffee_shop_obj.allow_reservation,
            'zero_lactose_options': coffee_shop_obj.zero_lactose_options,
            'gluten_free_options': coffee_shop_obj.gluten_free_options,
            'has_parking': coffee_shop_obj.has_parking,
            'accessibility': coffee_shop_obj.accessibility,
        }
        
        # Adiciona o coffee shop ao array de coffee shops
        coffee_shops.append(coffee_shop_data)
    
    # Ordena as babás pelo atributo favorited
    coffee_shops.sort(key=lambda x: x['favorited'], reverse=True)

    print(coffee_shops)
    if 'Sozinho' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['alone']]

    if 'Em grupo' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['has_meeting_room']]

    if 'Ambiente silencioso' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['has_silent_environment']]

    if 'Possibilidade de reserva' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['allow_reservation']]

    if 'veggie' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['vegan_options']]

    if 'zero-lactose' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['zero_lactose_options']]

    if 'gluten free' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['gluten_free_options']]

    if 'estacionamento' in request.GET:
 
        coffee_shops = [x for x in coffee_shops if x['has_parking']]        

    if 'acessibilidade' in request.GET:
        coffee_shops = [x for x in coffee_shops if x['accessibility']]
    

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

    # Buscar as reviews da cafeteria, limitando a 3
    reviews = Review.objects.filter(coffee_shop_id=pk).order_by('-score')[:3]

    # Adiciona as reviews ao coffee_shop_obj
    coffee_shop_obj.reviews = reviews

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

@login_required
def myprofile(request):
    user = request.user
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user=user)
    reservations = Reservation.objects.filter(user=user)
    
    coffee_shops = []
    
    # Inicializa o array de coffee shops favoritos
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
    reservations_with_costs = []  # Lista de tuplas (reserva, custo)
    for reservation in reservations:
        duration = float(reservation.duration)
        cost_var = float(reservation.cafe.reservation_cost)
        cost =  cost_var * duration/60
        reservations_with_costs.append((reservation, cost))
        
    context = {
        'coffee_shops': coffee_shops,
        'reservations_with_costs': reservations_with_costs,
        'user': user,
        
    }

    return render(request, 'myprofile.html', context)

def coffee_shop_reviews(request, pk):
    coffee_shop_obj = get_object_or_404(coffee_shop, pk=pk)

    #buscando reviews pelo id da cafeteria
    reviews = Review.objects.filter(coffee_shop_id=pk)

    # transformar a data em formato dd/mm/aaaa
    for review in reviews:
        review.created_at = review.created_at.strftime('%d/%m/%Y')

    # contar a quantidade de reviews
    reviews_count = reviews.count()

    # adicionar a quantidade de reviews ao coffee_shop_obj
    coffee_shop_obj.count = reviews_count

    return render(request, 'coffee_shop_reviews.html', {'coffee_shop': coffee_shop_obj, 'reviews': reviews})

@login_required
def new_review(request, pk):
    coffee_shop_obj = get_object_or_404(coffee_shop, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            if 0 <= review.score <= 5:
                review.user = request.user
                review.coffee_shop = coffee_shop_obj
                review.save()
                return redirect('coffee_shop_reviews', pk=coffee_shop_obj.pk)
            else:
                form.add_error('score', 'A nota deve ser entre 0 e 5.')
    else:
        form = ReviewForm()
    return render(request, 'new_review.html', {'form': form, 'coffee_shop': coffee_shop_obj})
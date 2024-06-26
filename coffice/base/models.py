from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class coffee_shop(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=3.0)
    has_silent_environment = models.BooleanField(default=False)
    cnpj = models.CharField(max_length=100, primary_key=True)
    allow_reservation = models.BooleanField(default=False)
    reservation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    coffee_spotlight = models.CharField(max_length=100)
    internet_speed = models.DecimalField(max_digits=10, decimal_places=2)
    vegan_options = models.BooleanField(default=False) 
    zero_lactose_options = models.BooleanField(default=False)
    gluten_free_options = models.BooleanField(default=False)
    accessibility  = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_meeting_room = models.BooleanField(default=False)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15, default='00000-000')
    phone = models.CharField(max_length=20, default='(00) 0000-0000')
    instagram = models.CharField(max_length=100, default='@coffice')
    site_url = models.URLField(max_length=100, default='https://coffice.com.br')
    alone = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.cnpj
    

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('C', 'Confirmada'),
        ('X', 'Cancelada'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(coffee_shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    duration = models.IntegerField(help_text="Duração em minutos")
    num_people = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"Reserva de {self.name} em {self.cafe.name} para {self.num_people} pessoas"
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14) 
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=9)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    
class Favorite(models.Model):
    coffee = models.ForeignKey(coffee_shop, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)

    class Meta:
        unique_together = ('coffee', 'user')

    def __str__(self):
        return f'{self.coffee} - {self.user}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_shop = models.ForeignKey(coffee_shop, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
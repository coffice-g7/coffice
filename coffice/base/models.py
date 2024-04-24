from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class coffee_shop(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=3.0)

    cnpj = models.CharField(max_length=100)
    allow_reservation = models.BooleanField(default=False)
    reservation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    coffee_spotlight = models.CharField(max_length=100)
    internet_speed = models.DecimalField(max_digits=10, decimal_places=2)
    vegan_options = models.BooleanField(default=False) 
    zero_lactose_options = models.BooleanField(default=False)
    gluten_free_options = models.BooleanField(default=False)
    accessibility  = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)

    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cnpj
    
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14) 
    phone_number = models.CharField(max_length=15)  
    ##profile_pic = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return self.user.username
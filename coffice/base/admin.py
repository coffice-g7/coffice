from django.contrib import admin
from .models import coffee_shop
from .models import Cliente
from .models import Reservation

# Register your models here.
admin.site.register(coffee_shop)
admin.site.register(Cliente)
admin.site.register(Reservation)
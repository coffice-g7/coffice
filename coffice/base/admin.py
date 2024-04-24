from django.contrib import admin
from .models import coffee_shop
from .models import Cliente

# Register your models here.
admin.site.register(coffee_shop)
admin.site.register(Cliente)
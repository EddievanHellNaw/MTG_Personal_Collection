from django.contrib import admin
from .models import Card 

class CardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'color' ,'foil' , 'in_deck','price')

# Register your models here.
admin.site.register(Card, CardsAdmin)
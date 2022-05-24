from django.contrib import admin
from .models import Card 

class CardsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'effect', 'foil', 'card_condition', 'in_deck','price')

# Register your models here.
admin.site.register(Card, CardsAdmin)
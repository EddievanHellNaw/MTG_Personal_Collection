from unittest import result
from django.shortcuts import render
from card_list.models import Card
import django_filters
from . import scrapper

# Create your views here.
def main (request):
    results = CardFilter(request.GET, queryset=Card.objects.all())
    cards = Card.objects.all()
    scrapper.schedule_price_update(cards)
    return render(request, 'home.html', {'results': results})

def cardFilter(request):
    results = CardFilter(request.GET, queryset=Card.objects.all())
    return render(request, 'card_search.html', {'results':results})
    

class CardFilter(django_filters.FilterSet):
    foil=django_filters.BooleanFilter(field_name='foil')
    class Meta:
        model = Card
        fields = {'name': ['contains'],
                  'expansion_name':['contains'],
                  'color':['contains'],
                  'card_type':['contains']
        }

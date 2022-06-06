from django.shortcuts import render
from card_list.models import Card
import django_filters

# Create your views here.
def index (request):
    pass

class CardFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    expansion=django_filters.CharFilter(field_name='expansion_name', lookup_expr='icontains')
    color=django_filters.CharFilter(field_name='color', lookup_expr='icontains')
    card_type=django_filters.CharFilter(field_name='card_type', lookup_expr='icontains')
    foil=django_filters.BooleanFilter(field_name='foil', lookup_expr='True')

    class Meta:
        model = Card
        fields = ['expansion_name','name','color','foil','card_type']
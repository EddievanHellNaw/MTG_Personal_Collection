from django.shortcuts import render
from .models import Card


# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, 'card_list/index.html', {'cards': cards})

def card_search(request):
    if request.method == "POST":
        query_name = request.POST.get('name',None)
        if query_name:
            results = Card.objects.filter(name__contains=query_name)
            return render(request,'card_list/card_search.html',{"results":results})
    return render(request,'card_list/card_search.html')
from django.urls import path, re_path
from django_filters.views import FilterView
from card_list.models import Card
from . import views




urlpatterns = [
    path("",views.main,name="home"),
    path("search/",views.cardFilter,name="card_search"),
    re_path(r'^list$', FilterView.as_view(model=Card)),
]
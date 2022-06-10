from django.urls import path, re_path
from django_filters.views import FilterView
from card_list.models import Card
from . import views




urlpatterns = [
    path("",views.main,name="home"),
    path("search/",views.cardFilter,name="card_search"),
    path('json_data/', views.post_json, name="json_data_view"),
    re_path(r'^list$', FilterView.as_view(model=Card)),
]
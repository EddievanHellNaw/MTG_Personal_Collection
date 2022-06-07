from django.urls import path, re_path
from .views import HomePageView, SearchResultsView
from . import views



urlpatterns = [
    path('search/',SearchResultsView.as_view(), name="card_search"),
    path("", HomePageView.as_view(), name="home"),
    re_path(r'^list$', views.index),
]
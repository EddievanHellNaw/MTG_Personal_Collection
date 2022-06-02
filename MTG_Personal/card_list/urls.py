from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('card_search/', views.search_by_name, name="card_search"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
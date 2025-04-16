from django.urls import path
from .views import PokemonAPIView

urlpatterns = [
    path('pokemon/<str:pokemon_name>/', PokemonAPIView.as_view()),
]

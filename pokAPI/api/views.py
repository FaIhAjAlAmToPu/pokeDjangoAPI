from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

class PokemonAPIView(APIView):
    def get(self, request, pokemon_name):
        cache_key = f"pokemon_{pokemon_name}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour
            return Response(data)

        return Response({"error": "Pokémon not found"}, status=404)

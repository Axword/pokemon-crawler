"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from pokemon.views import get_pokemons_list, get_pokemon_details_by_name

urlpatterns = [
    path('api/pokemon/<str:pokemon_name>/',
         get_pokemon_details_by_name, name="pokemon-detail"),
    path("api/pokemons/", get_pokemons_list, name="pokemon-list",), ]

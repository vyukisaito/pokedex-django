from django.shortcuts import render
import urllib.request
import json


def index(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace(' ', '&20')
        url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        url_pokeapi.add_header('User-Agent', 'charmander')

        source = urllib.request.urlopen(url_pokeapi).read()

        list_of_data = json.loads(source)

        data = {
            "number": str(list_of_data['id']),
            "name": str(list_of_data['name']).capitalize(),
            "height": str(list_of_data['height']),
            "weight": str(list_of_data['weight']),
            "sprite": str(list_of_data['sprites']['front_default']),
        }

        print(data)
    else:
        data = {}

    return render(request, 'home.html', data)
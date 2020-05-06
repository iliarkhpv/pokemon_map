import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/" \
                    "latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(name=pokemon.id):
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title, request.build_absolute_uri(pokemon.image.url))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    print(pokemon.next_evolution.all())
    pokemon_description = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.image.url,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
         }
    if pokemon.next_evolution is not None:
        for next_evolution in pokemon.next_evolution.all():
            pokemon_description['next_evolution'] = {
                "title_ru": next_evolution.title,
                "pokemon_id": next_evolution.id,
                "img_url": next_evolution.image.url
            }
    if pokemon.previous_evolution is not None:
        pokemon_description['previous_evolution'] = {
                'title_ru': pokemon.previous_evolution.title,
                'pokemon_id': pokemon.previous_evolution.id,
                'img_url': pokemon.previous_evolution.image.url
            }

    if pokemon.id == int(pokemon_id):
        requested_pokemon = pokemon
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in PokemonEntity.objects.filter(name=requested_pokemon.id):
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon.title, request.build_absolute_uri(pokemon.image.url))


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_description})

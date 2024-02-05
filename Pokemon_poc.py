import pytest
import requests


# Helper function to make a request to the Pokemon API
def get_pokemon_api_data(url):
    response = requests.get(url)
    # Raise an error for bad responses
    response.raise_for_status()
    return response.json()


# Question 1
def test_pokemon_type_api_response():
    url = 'https://pokeapi.co/api/v2/type'
    data_Q1 = get_pokemon_api_data(url)
    # Ensure response is a dictionary => json format
    assert isinstance(data_Q1, dict)
    # Ensure there are exactly 20 different Pokémon types
    assert data_Q1['count'] == 20
    return data_Q1


# Question 2
def test_fire_type_pokemon():
    data_Q1 = test_pokemon_type_api_response()
    fire_type_url = None
    for result in data_Q1['results']:
        if result['name'] == 'fire':
            fire_type_url = result['url']
            # Break the loop once 'fire' type is found
            break
    # Ensure 'fire' type URL is found
    assert fire_type_url is not None

    data_Q2 = get_pokemon_api_data(fire_type_url)

    for result in data_Q2['pokemon']:
        if result['pokemon']['name'] == 'charmander':
            charmander_present = True

        if result['pokemon']['name'] == 'bulbasaur':
            bulbasaur_present = True
        else:
            bulbasaur_present = False

    # Validate charmander is  in the list
    assert charmander_present

    # Validate bulbasaur is not in the list
    assert not bulbasaur_present
    return data_Q2


# Question 3
def test_heaviest_fire_type_pokemon():
    data_Q3 = test_fire_type_pokemon()

    heaviest_pokemon = {
        'charizard-gmax': 10000,
        'cinderace-gmax': 10000,
        'coalossal-gmax': 10000,
        'centiskorch-gmax': 10000,
        'groudon-primal': 9997
    }
    weights_dict = {}
    for pokemon in data_Q3['pokemon']:
        name_p = pokemon['pokemon']['name']
        weight_p = get_pokemon_api_data(pokemon['pokemon']['url'])['weight']
        weights_dict[name_p] = weight_p

    heaviest = dict(sorted(weights_dict.items(), key=lambda item: item[1], reverse=True)[:5])

    if heaviest == heaviest_pokemon:
        print("The two dictionaries are equal")
    else:
        print("The two dictionaries are not equal")


if __name__ == '__main__':
    pytest.main(['-v'])

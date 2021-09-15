import requests

pokemon_id = [1, 2, 3, 4, 5, 6]
with open('pokemon.txt', 'w') as pokemon_file:
    pokemon_file.write('Pokemon names and moves:')

for pokemon in pokemon_id:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    response = requests.get(url)
    pokemon_data = response.json()
    with open('pokemon.txt', 'a') as pokemon_file:
        pokemon_file.write('\n\nID: {}'.format(pokemon))
        pokemon_file.write('\nName: {}'.format(pokemon_data['name']))
        pokemon_file.write('\nMoves:')
        for moves in pokemon_data['moves']:
            pokemon_file.write('\n' + moves['move']['name'])

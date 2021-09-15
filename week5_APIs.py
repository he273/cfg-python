import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
nasa_data = response.json()
print(nasa_data)
print(nasa_data.keys())

import requests
import pprint

pokemon_id = input('Enter the pokemon id: ')
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)

response = requests.get(url)
pokemon_data = response.json()
#print(pokemon_data)
pprint.pprint(pokemon_data)
print(pokemon_data['name'])
for moves in pokemon_data['moves']:
    print(moves['move']['name'])

#Prinz Magtulis
#Homework #3 Part 1
#November 7, 2021

import requests

#Pokemon 55 and height
response = requests.get("https://pokeapi.co/api/v2/pokemon/55")
print(response.json())
pokemon_55 = response.json()
#print(pokemon_55)
#print(pokemon_55.keys())
print("The 55th pokemon on the pokedex is", pokemon_55['name'])
print("Golduck stands", pokemon_55['height'], "decimeters.")

#Pokemon versions
response = requests.get("https://pokeapi.co/api/v2/version/")
print(response.json())
pokemon_versions = response.json()
#print(pokemon_versions)
#print(pokemon_versions.keys())
print("There have been", pokemon_versions['count'], "versions of Pokemon so far.")

#Electric type pokemons
response = requests.get("https://pokeapi.co/api/v2/type/13/")
print(response.json())
pokemon_electric = response.json()
#print(pokemon_electric)
#print(pokemon_electric.keys())
electric_type = pokemon_electric['pokemon']
#print(electric_type)
print("There are", len(electric_type), "electric pokemons.")
for electric in electric_type:
    #print(electric)
    #print(electric.keys())
    thunder = electric['pokemon']
    #print (names)
    #print(names.keys())
    name = thunder ['name']
    print (name)

#Electric type in Korean name
pokemon_electric = response.json()
print(pokemon_electric)
#print(pokemon_electric.keys())
korean = pokemon_electric['names']
#print (korean)
for korean_translate in korean:
    if korean_translate ['language']['name']== 'ko':
#Nested dictionary? Not yet taught.
        print ("Electric-type Pokemons are called", korean_translate['name'], "in Korean.")

#Eevee or Pikachu on speed
eevee = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(eevee.json())
print(pikachu.json())
eevee_speed = eevee.json()
pikachu_speed = pikachu.json()
for speed in eevee_speed and pikachu_speed:
    stats_eevee = eevee_speed ['stats']
    stats_pikachu = pikachu_speed ['stats']
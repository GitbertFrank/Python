import requests

baseUrl = "https://pokeapi.co/api/v2/"

def getPokeInfo(name):
    url = f"{baseUrl}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokeData = response.json()
        return pokeData
    else:
        print(f"failed to retrieve data {response.status_code}")

pokeName = "charizard"

pokeInfo = getPokeInfo(pokeName)

if pokeInfo:
    print(f"Name: {pokeInfo["name"].capitalize()}")
    print(f"ID: {pokeInfo["id"]}")
    print(f"Height: {pokeInfo["height"]}")
    print(f"Weight: {pokeInfo["weight"]}")
    print(f"type: {pokeInfo["types"]}")



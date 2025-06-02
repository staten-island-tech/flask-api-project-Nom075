import requests

response = requests.get("https://raw.githubusercontent.com/WhalenSITHS/Pokedex-Python-Starter/refs/heads/main/pokedex.json")

data = response.json()



for pokemon in data:
    if (pokemon['type'][0][:1] == pokemon['type'][1][:1]):
        print(pokemon['name'['english']])


        



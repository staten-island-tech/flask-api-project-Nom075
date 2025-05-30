from flask import Flask, render_template
import requests
from functools import lru_cache

app = Flask(__name__)

@lru_cache()
def fetch_item_images():
    item_response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/items.json")
    item_images = {}
    if item_response.status_code == 200:
        items_data = item_response.json()
        for item in items_data:
            item_images[item['name'].lower()] = item.get('image', 'N/A')
    return item_images

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/items")
def items():
    response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/items.json")
    recipes_response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/recipes.json")
    item_images = fetch_item_images()
    air_image = "https://webstockreview.net/images/lace-clipart-square-18.png"

    if response.status_code == 200 and recipes_response.status_code == 200:
        data = response.json()
        recipes_data = recipes_response.json()
        recipe_lookup = {r['item'].lower(): r['recipe'] for r in recipes_data}
        print(recipe_lookup)
        items = []
        for item in data:
            item_name_lower = item['name'].lower()
            raw_recipe = recipe_lookup.get(item_name_lower)

            # Enrich recipe with image info
            if raw_recipe:
                processed_recipe = []
                for i in range(9):
                    ingredient = raw_recipe[i] if i < len(raw_recipe) else None

                    if ingredient:
                        if isinstance(ingredient, list):
                            ing_name = ingredient[0]
                        else:
                            ing_name = ingredient

                        processed_recipe.append({
                            'name': ing_name,
                            'image': item_images.get(ing_name.lower(), air_image) if ing_name else air_image
                        })
                    else:
                        processed_recipe.append({
                            'name': '',
                            'image': air_image
                        })
            else:
                processed_recipe = None

            items.append({
                'name': item['name'],
                'description': item.get('description', 'N/A'),
                'image': item.get('image', 'N/A'),
                'renewable': item.get('renewable', 'N/A'),
                'stackSize': item.get('stackSize', 'N/A'),
                'recipe': processed_recipe
            })

        return render_template("items.html", items=items)
    else:
        return "Failed to fetch item or recipe data", 500



if __name__ == '__main__':
    app.run(debug=True)


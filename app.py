from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch item images from items.json
def fetch_item_images():
    item_response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/items.json")
    item_images = {}
    if item_response.status_code == 200:
        items_data = item_response.json()
        for item in items_data:
            item_images[item['name'].lower()] = item.get('image', 'N/A')  # Map item name to image
    return item_images

# --- HOME PAGE (option selector) ---
@app.route("/")
def home():
    return render_template("home.html")

# --- ITEMS PAGE ---
@app.route("/items")
def items():
    response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/items.json")
    if response.status_code == 200:
        data = response.json()
        items = []
        for item in data:
            items.append({
                'name': item['name'],
                'description': item.get('description', 'N/A'),
                'image': item.get('image', 'N/A'),
                'renewable': item.get('renewable', 'N/A'),
                'stackSize': item.get('stackSize', 'N/A')
            })
        return render_template("items.html", items=items)
    else:
        return "Failed to fetch item data", 500

# --- RECIPES PAGE ---
@app.route("/recipes")
def recipes():
    recipes_response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/recipes.json")
    item_images = fetch_item_images()  # Get the item image dictionary

    if recipes_response.status_code == 200:
        recipes = recipes_response.json()

        # Set up a placeholder for air image (this can be a blank image)
        air_image = "https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/master/data/images/air.png"  # Placeholder for air

        # Add image URLs to each recipe item and ingredient
        for recipe in recipes:
            # Set up the image URL for the result item (e.g., Acacia Boat)
            recipe['item_image'] = item_images.get(recipe['item'].lower(), 'N/A')  # Use item name to get image

            # Add the ingredient images for the crafting grid
            for i, ingredient in enumerate(recipe['recipe']):
                if ingredient:
                    if isinstance(ingredient, str):  # Check if ingredient is a string
                        recipe['recipe'][i] = {
                            'name': ingredient,
                            'image': item_images.get(ingredient.lower(), air_image)  # Use ingredient name to get image
                        }
                    else:
                        recipe['recipe'][i] = {'name': 'Empty', 'image': air_image}  # Empty slot (null value)
                else:
                    recipe['recipe'][i] = {'name': 'Empty', 'image': air_image}  # Empty slot (null value)

        return render_template("recipes.html", recipes=recipes)
    else:
        return "Failed to fetch recipe data", 500

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the list of items from the new API
    response = requests.get("https://raw.githubusercontent.com/anish-shanbhag/minecraft-api/refs/heads/master/data/items.json")
    
    if response.status_code == 200:
        data = response.json()
        
        # Create a list to hold item details
        items = []
        
        for item in data:
            items.append({
                'name': item['name'],
                'description': item.get('description', 'N/A'),
                'image': item.get('image', 'N/A'),
                'renewable': item.get('renewable', 'N/A'),
                'stackSize': item.get('stackSize', 'N/A')
            })
        
        # Send the list of items to the index.html page
        return render_template("index.html", items=items)
    else:
        return "Failed to fetch item data", 500

if __name__ == '__main__':
    app.run(debug=True)
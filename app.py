from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the list of countries from the API
    response = requests.get("https://country-cities.herokuapp.com/api/v0.1/countries")
    
    if response.status_code == 200:
        data = response.json()
        country_list = data['results']
        
        # Create a list to hold country details
        countries = []
        
        for country in country_list:
            countries.append({
                'name': country['name'],
                'capital': country.get('capital', 'N/A'),
                'population': country.get('population', 'N/A'),
                'flag': country.get('flag', 'N/A')
            })
        
        # Send the list of countries to the index.html page
        return render_template("index.html", countries=countries)
    else:
        return "Failed to fetch country data", 500

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = {}
    winter_facts = [
        "Snowflakes can take up to an hour to fall from a cloud to the ground.",
        "The record for the most snow in a single 24-hour period is 192.5 cm inches.",
        "Winter solstice is the shortest day of the year.",
        "Some animals hibernate to survive the cold months."
    ]

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": "City not found. Please try again."}

    return render_template("index.html", weather=weather_data, facts=winter_facts)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

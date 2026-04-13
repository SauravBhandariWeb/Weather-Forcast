from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "0bcb63c6b10d63bcea558318406c3d66"

@app.route("/", methods=["GET", "POST"])
def home():
        city = "Jaipur"
        weather = None

        if request.method == "POST":
            city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") == 200:
            weather = {
            "city": data["name"],
                "country": data["sys"]["country"],
                "temp": round(data["main"]["temp"]),
                "temp_min": round(data["main"]["temp_min"]),
                "temp_max": round(data["main"]["temp_max"]),
                "feels_like": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind": round(data["wind"]["speed"]),
                "main": data["weather"][0]["main"],
                "icon": data["weather"][0]["icon"],
                "date": datetime.utcfromtimestamp(data["dt"]).strftime('%A, %d %B %Y')
            }

        return render_template("index.html", weather=weather)



if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=0)
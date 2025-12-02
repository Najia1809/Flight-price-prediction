from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join("static", "model", "flight_price_model.pkl")
model = pickle.load(open(model_path, "rb"))

# ✅ Encoding dictionaries (as in your preprocessing)
airline_map = {
    "SkyAir": 1,
    "CloudJet": 2,
    "JetWorld": 3,
    "GlobalFly": 4,
    "AirNova": 5
}

source_map = {
    "Dubai": 0,
    "London": 1,
    "Tokyo": 2,
    "Paris": 3,
    "Singapore": 4,
    "New York": 5,
    "Berlin": 6
}

destination_map = {
    "London": 0,
    "Tokyo": 1,
    "Paris": 2,
    "Dubai": 3,
    "Singapore": 4,
    "Toronto": 5,
    "New York": 6,
    "Hong Kong": 7
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get user input
    airline_name = request.form["Airline"]
    source_name = request.form["Source"]
    destination_name = request.form["Destination"]

    journey_day = int(request.form["Journey_Day"])
    journey_month = int(request.form["Journey_Month"])

    dep_hour = int(request.form["Dep_Hour"])
    dep_min = int(request.form["Dep_Min"])
    arr_hour = int(request.form["Arr_Hour"])
    arr_min = int(request.form["Arr_Min"])

    duration = float(request.form["Duration"])
    stops = int(request.form["Stops"])
    flight_class = int(request.form["Class"])

    # Encode user input to numeric values
    airline = airline_map[airline_name]
    source = source_map[source_name]
    destination = destination_map[destination_name]

    # Convert hours + minutes to decimal hours
    dep_time = dep_hour + dep_min / 60
    arr_time = arr_hour + arr_min / 60

    # Date_of_Journey as in your training data
    date_of_journey = journey_day * 100 + journey_month

    # Create DataFrame with correct column names
    features = pd.DataFrame([[
        airline,
        source,
        destination,
        date_of_journey,
        dep_time,
        arr_time,
        duration,
        stops,
        flight_class
    ]], columns=["Airline","Source","Destination","Date_of_Journey",
                 "Departure_Time","Arrival_Time","Duration","Stops","Class"])

    # Predict price
    prediction = model.predict(features)[0]

    return render_template("index.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)

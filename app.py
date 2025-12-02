from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# ✅ Load Model
import os
import pickle

model_path = os.path.join("static", "model", "flight_price_model.pkl")
model = pickle.load(open(model_path, "rb"))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
@app.route("/predict", methods=["POST"])
def predict():
    airline = request.form["Airline"]
    source = request.form["Source"]
    destination = request.form["Destination"]

    journey_day = int(request.form["Journey_Day"])
    journey_month = int(request.form["Journey_Month"])

    dep_hour = int(request.form["Dep_Hour"])
    arr_hour = int(request.form["Arr_Hour"])

    duration = float(request.form["Duration"])
    stops = int(request.form["Stops"])

    # ✅ FINAL 9 FEATURES ORDER (MATCHED TO MODEL)
    features = [[
        journey_day,
        journey_month,
        dep_hour,
        arr_hour,
        duration,
        stops,
        hash(airline) % 10,
        hash(source) % 10,
        hash(destination) % 10
    ]]

    prediction = model.predict(features)[0]

    return render_template("index.html", prediction_text=f"Predicted Price: {round(prediction,2)}")


if __name__ == "__main__":
    app.run(debug=True)

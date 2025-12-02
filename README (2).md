# ✈️ Flight Price Prediction Web Application

A full-stack Machine Learning web application that predicts airline
flight prices based on user input using a trained Random Forest
regression model. The web interface is built with Flask, HTML, and CSS.

------------------------------------------------------------------------

## 🚀 Project Features

- Predicts **flight ticket prices**
- Uses **Machine Learning (Random Forest Regressor)**
- Inputs include:
  - Airline
    - Source
    - Destination
    - Journey Date
    - Departure & Arrival Time
    - Duration
    - Stops
    - Class (Economy/Business)
- Model saved using Pickle
- Fully integrated end-to-end ML + Web App

------------------------------------------------------------------------

## 🧠 Machine Learning Model

- Algorithm: Random Forest Regressor
- Target Variable: `Price`
- Total Features Used: 9
- Dataset Size: \~300 rows
- Accuracy (R² Score): \~97%

The model was trained in Jupyter Notebook and exported using Pickle.

------------------------------------------------------------------------

## 🛠️ Tech Stack

- Python
- Flask (Web Framework)
- Pandas, NumPy
- Scikit-learn
- Pickle
- HTML, CSS, JavaScript

------------------------------------------------------------------------

## 📁 Project Structure

Flight-price-webapp/ ├── static/ │ ├── css/ │ │ └── style.css │ ├── js/
│ │ └── scripts.js │ └── model/ │ └── flight_price_model.pkl │ ├──
templates/ │ └── index.html │ ├── venv/ ├── app.py ├── requirements.txt
└── README.md

------------------------------------------------------------------------

## ▶️ How to Run This Project Locally

### 1️⃣ Clone the Repository

    git clone https://github.com/Najia1809/Flight-price-prediction.git
    cd flight-price-prediction-webapp

------------------------------------------------------------------------

### 2️⃣ Create Virtual Environment

    python -m venv venv

Activate:

Mac / Linux

    source venv/bin/activate

Windows

    venv\Scripts\activate

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

### 4️⃣ Run the Flask App

    python app.py

Open in browser:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📊 Model Input Features

- Airline
- Source
- Destination
- Journey Day
- Journey Month
- Departure Hour
- Departure Minute
- Duration
- Stops
- Class

------------------------------------------------------------------------

## ✅ Output

The app predicts the **estimated flight ticket price** based on your
input.

------------------------------------------------------------------------

## 📌 Important Notes

- The ML model expects **numerical encoded features**.
- Do not change input names without updating `app.py`.
- This project is intended for **academic and learning purposes**.

------------------------------------------------------------------------

## 👩‍💻 Developer

Developed by **Najia Khan**\
BS Artificial Intelligence\
Machine Learning & Web Development Project

------------------------------------------------------------------------

## License

This project is for educational use only.

from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('car_price_model.pkl', 'rb'))

# Load CSV for dropdowns
data = pd.read_csv("car_prediction_data.csv")

car_names = sorted(data["Car_Name"].unique())
fuel_types = sorted(data["Fuel_Type"].unique())
seller_types = sorted(data["Seller_Type"].unique())
transmissions = sorted(data["Transmission"].unique())
owners = sorted(data["Owner"].unique())
years = sorted(data["Year"].unique())

@app.route("/")
def home():
    return render_template(
        "index.html",
        car_names=car_names,
        fuel_types=fuel_types,
        seller_types=seller_types,
        transmissions=transmissions,
        owners=owners,
        years=years
    )

@app.route("/predict", methods=["POST"])
def predict():

    year = int(request.form["year"])
    present_price = float(request.form["present_price"])
    kms_driven = int(request.form["kms_driven"])
    fuel_type = request.form["fuel_type"]
    seller_type = request.form["seller_type"]
    transmission = request.form["transmission"]
    owner = int(request.form["owner"])

    present_price_log = np.log(present_price + 1)

        # Initialize all columns to 0
    fuel_diesel = 0
    fuel_petrol = 0
    seller_individual = 0
    transmission_manual = 0

    # Set the correct column to 1 based on user input
    if fuel_type == "Diesel":
        fuel_diesel = 1
    elif fuel_type == "Petrol":
        fuel_petrol = 1
    # For CNG, both fuel_diesel and fuel_petrol remain 0

    if seller_type == "Individual":
        seller_individual = 1
    # Dealer → 0

    if transmission == "Manual":
        transmission_manual = 1
    # Automatic → 0

    final_features = np.array([[year, present_price, kms_driven, owner, 
                            present_price_log,
                            fuel_diesel, fuel_petrol,
                            seller_individual,
                            transmission_manual]])



    prediction = model.predict(final_features)[0]  # correct





    return render_template(
        "index.html",
        prediction_text=f"Estimated Car Price: ₹ {round(prediction,2)} Lakhs",
    
        fuel_types=fuel_types,
        seller_types=seller_types,
        transmissions=transmissions,
        owners=owners,
        years=years
    )

if __name__ == "__main__":
    app.run(debug=True)

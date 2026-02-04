#  Car Price Prediction Web App

A **Machine Learning–powered web application** that predicts the **resale price of a car** based on user inputs such as present price, kilometers driven, age, fuel type, seller type, and transmission.  
The app is built using **Python, Flask, and Scikit-learn** with a clean **dark-themed UI**.

---

##  Project Overview

Predicting car resale prices is a real-world regression problem.  
This project demonstrates an **end-to-end ML workflow**, including:

- Data preprocessing & feature engineering  
- Model training and evaluation  
- Hyperparameter tuning  
- Model serialization using Pickle  
- Deployment using Flask  
- User-friendly web interface  

---

##  Demo Video


https://github.com/user-attachments/assets/baeca443-a8fe-47bb-86a7-0dabc76720af


##  Machine Learning Model

- **Algorithm Used:** Random Forest Regressor (Hyperparameter Tuned)  
- **Target Variable:** `Selling_Price`  
- **Evaluation Metric:** R² Score ≈ 0.95  
- **Feature Scaling:** StandardScaler  

###  Model Input Features (in order)

['Present_Price',
'Kms_Driven',
'Owner',
'Fuel_Type_Diesel',
'Fuel_Type_Petrol',
'Seller_Type_Individual',
'Transmission_Manual']



---

##  Dataset Description

The dataset contains historical car sales data with the following attributes:

- **Car_Name** – Name of the car  
- **Year** – Year of manufacture  
- **Present_Price** – Showroom price  
- **Kms_Driven** – Distance driven (in km)  
- **Fuel_Type** – Petrol / Diesel / CNG  
- **Seller_Type** – Dealer / Individual  
- **Transmission** – Manual / Automatic  
- **Owner** – Number of previous owners  
- **Selling_Price** – Target variable (resale price)  

---

##  Technologies Used

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas, NumPy  
- **Model Storage:** Pickle  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS (Dark Theme UI)  
- **IDE/Tools:** Jupyter Notebook, VS Code  

---

##  Project Structure

car-price-prediction/

│

├── model_training.ipynb


├── car_price_model.pkl

├── app.py

├── car_data.csv

├── templates/

│ └── index.html


├── static/

│ └── style.css


└── README.md



---

##  Model Training Workflow

1. Load dataset  
2. Handle missing values  
3. Perform feature engineering  
4. Encode categorical variables  
5. Split into training and testing sets  
6. Train Random Forest model  
7. Tune hyperparameters using GridSearchCV  
8. Save trained model using Pickle  

---

## Output

The application predicts the **estimated resale price of the car** based on user-provided values and displays the result instantly on the web interface.

---

##  Advantages

- Accurate predictions  
- Easy-to-use interface  
- Real-time inference  
- Helps buyers and sellers make informed decisions  
- Demonstrates full ML lifecycle  

---

##  Future Enhancements

- Add more ML models (XGBoost, Gradient Boosting)  
- Integrate real-time car marketplace data  
- Deploy on cloud (AWS / Render / Heroku)  
- Add user authentication  
- Improve UI with charts and visualizations  

---

## Author

**Aparna N**  
**MCA**  
**Aspiring Data Scientist**

---

## 📜 License

This project is developed for **educational purposes only**.

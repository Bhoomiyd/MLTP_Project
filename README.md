# MLTP_Project

 Weather Prediction Web App

A simple Machine Learning project that predicts **temperature** based on weather conditions using **Linear Regression**.
This project is built using **Python, Flask, and HTML/CSS.

 Project Overview

This web application allows users to enter:

* Humidity (%)
* Wind Speed (km/h)
* Pressure (hPa)

The trained ML model predicts the **temperature (°C)** instantly and displays it on a web interface.

 Features

* Simple and user-friendly web interface
*  Machine Learning model (Linear Regression)
*  Input validation with real-world ranges
*  Instant prediction results
*  Professional UI using HTML & CSS
*  Error handling for invalid inputs

---

Technologies Used

* **Python**
* **Flask** (Web framework)
* **Pandas** (Data handling)
* **Scikit-learn** (ML model)
* **NumPy**
* **HTML & CSS**

---

Dataset

* Contains **1000 records**
* Columns:

  * Temperature
  * Humidity
  * Wind Speed
  * Pressure
  * Rainfall

---

 How It Works

1. Dataset is loaded and preprocessed
2. Linear Regression model is trained
3. Model is saved using `pickle`
4. Flask app loads the model
5. User inputs are taken from HTML form
6. Prediction is displayed on the webpage

---

 How to Run the Project
 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-prediction-app.git
cd weather-prediction-app
```

 2. Install dependencies

```bash
pip install flask pandas scikit-learn numpy
```

 3. Train the model

```bash
python model.py
```

 4. Run the application

```bash
python app.py
```

 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
weather_project/
│
├── app.py
├── model.py
├── model.pkl
├── weather_dataset_1000.csv
└── templates/
    └── index.html
```

---

 Model Details

* Algorithm: **Linear Regression**
* Target: Temperature
* Input Features:

  * Humidity
  * Wind Speed
  * Pressure

---

 Future Enhancements

*  Integrate live weather API
*  Use advanced models (Random Forest, XGBoost)
*  Add data visualization charts
*  Deploy the application online

---

Author
Bhoomika Y D

Acknowledgement

This project is created for learning purposes to understand:

* Machine Learning basics
* Web integration using Flask
* Real-time prediction systems

---



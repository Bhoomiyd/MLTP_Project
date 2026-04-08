import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("weather_dataset_1000.csv")

X = data[['humidity', 'wind_speed', 'pressure']]
y = data['temperature']

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained!")
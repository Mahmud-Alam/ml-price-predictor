import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import pickle

data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'price': [500000, 700000, 950000, 1350000, 2000000]
}

df = pd.DataFrame(data)

# model = LinearRegression()

# Use polynomial regression (degree 2)
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(df[['area']], df['price'])

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")

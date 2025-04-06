import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'price': [100000, 150000, 200000, 250000, 300000]
}

df = pd.DataFrame(data)

model = LinearRegression()
model.fit(df[['area']], df['price'])

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")

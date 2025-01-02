

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Carregar os dados
data = pd.read_csv('data.csv')
X = data[['x']].values
y = data['y'].values

# Treinar modelo
model = LinearRegression()
model.fit(X, y)

# Salvar o modelo
joblib.dump(model, 'model.pkl')
print("Modelo salvo em model.pkl")

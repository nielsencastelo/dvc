import pandas as pd
import numpy as np


np.random.seed(42)
x = np.random.rand(100, 1)
y = 3 * x[:, 0] + np.random.randn(100)

data = pd.DataFrame({'x': x[:, 0], 'y': y})
data.to_csv('data.csv', index=False)
print("Dados salvos em data.csv")

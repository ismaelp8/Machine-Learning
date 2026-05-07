from apafib import load_BCN_NO2
import pandas as pd

# Cargar los datos
data = load_BCN_NO2()
print(data.shape)
data.head()

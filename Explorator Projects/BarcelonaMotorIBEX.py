import pandas as pd
import numpy as np
from apafib import load_BCN_IBEX

data = load_BCN_IBEX()
print(data.head())
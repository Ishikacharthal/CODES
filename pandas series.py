import numpy as np
import pandas as pd

np.random.seed(42)

data = np.random.randint(1, 101, 10)

s = pd.Series(data)

print(s)
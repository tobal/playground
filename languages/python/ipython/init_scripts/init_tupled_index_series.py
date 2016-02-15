import pandas as pd
import numpy as np

input_dict = {('a','b'): 1, ('a','c'): 2, ('b','c'): 3}
index = input_dict.keys()
data = pd.Series(input_dict, index=index).sort_values(ascending=False)

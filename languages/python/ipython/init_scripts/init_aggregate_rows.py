import pandas as pd
import numpy as np

input_dict = {('a','b'): 1, ('a','c'): 2, ('b','c'): 3}
index = input_dict.keys()
data = pd.Series(input_dict, index=index).sort_values(ascending=False)
df = pd.DataFrame(data, columns=['count'])

df.insert(0, 'ngrams', df.index)
df = df.set_index([list(range(len(df.index)))])

def should_aggregate(first_ngram, second_ngram):
    if first_ngram[0] == second_ngram[0]:
        return True
    return False

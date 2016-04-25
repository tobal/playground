import pandas as pd
import numpy as np

input_dict = {('a','b'): 1, ('a','c'): 2, ('b','c'): 3, ('a','g'): 1}
index = input_dict.keys()
data = pd.Series(input_dict, index=index).sort_values(ascending=False)
df = pd.DataFrame(data, columns=['count'])

df.insert(0, 'ngrams', df.index)
index = list(range(len(df.index)))
df = df.set_index([index])
df['ix'] = index
df['remain'] = True

def aggre(df):
    df.apply(agg_df, axis='columns', args=(df,))

def agg_df(row, df):
    tupl = row['ngrams']
    ix = row['ix']
    df.loc[ix+1:][df.remain].apply(agg_subrow, axis=1, args=(ix, tupl, df))

def agg_subrow(subrow, ix, tupl, df):
    if not subrow.empty:
        if should_aggregate(subrow['ngrams'], tupl):
            df.loc[ix, 'count'] += subrow['count']
            df.loc[subrow['ix'], 'remain'] = False

def should_aggregate(first_ngram, second_ngram):
    if first_ngram[0] == second_ngram[0]:
        return True
    return False

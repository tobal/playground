# IPython log file

get_ipython().magic('run init_scripts/init_aggregate_rows.py')
df
df[['ngrams','count']]
def f(x):
    return x
df[['ngrams','count']].apply(f, axis='columns')
get_ipython().magic('logstart')
def f(x):
    return x

def f(x, y):
    return y

df[['ngrams','count']].apply(f, axis='columns', args=('csojj'))
def f(x, y, a, b, c, d):
    return y

df[['ngrams','count']].apply(f, axis='columns', args=('csojj'))
def f(x, y, a, b, c, d):
    return a

def f(x, y):
    return y

df[['ngrams','count']].apply(f, axis='columns', args=(6))
df[['ngrams','count']].apply(f, axis='columns', args=(6, ))
df[['ngrams','count']].apply(f, axis='columns', args=('csojj', ))
type(df[['ngrams','count']].apply(f, axis='columns', args=('csojj', )))
df

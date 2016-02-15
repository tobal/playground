# IPython log file

get_ipython().magic('logstart')
get_ipython().magic('run init_scripts/init_tupled_index_series.py')
data
df = pd.DataFrame(data)
df
def should_aggregate(first_ngram, second_ngram):
    if first_ngram[0] == second_ngram[0]:
        return True
    return False

should_aggregate( ('a'), ('a') )
should_aggregate( ('a'), ('b') )
should_aggregate( ('a', 'c'), ('b', 'c') )
should_aggregate( ('a', 'c'), ('a', 'b') )
get_ipython().magic('pinfo2 should_aggregate')
df
df.apply(should_aggregate)
def appex(*args):
    print(args)

df.apply(appex)
df.apply(lambda x: print(x))
df.apply(lambda x: print(dir(x)))
df.applymap(lambda x: print(dir(x)))
df.applymap(lambda x: print(x))
df.applymap(lambda x: x)
ixdf = df.set_index(range(len(df.index)))
ixdf = df.set_index(xrange(len(df.index)))
ixdf = df.set_index(list(range(len(df.index))))
ixdf = df.set_index([list(range(len(df.index)))])
ixdf
df
type(df)
get_ipython().magic('pinfo df.insert')
df.insert(0, 'ngrams', df.index)
df
ixdf = df.set_index([list(range(len(df.index)))])
ixdf
get_ipython().magic('pinfo2 should_aggregate')

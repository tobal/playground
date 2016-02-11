# IPython log file

get_ipython().magic('logstart')
get_ipython().system('cmd ls')
get_ipython().system('ls')
input_dict = {('a','b'): 10, ('a','c'): 20, ('b','c'): 30}
get_ipython().magic('pinfo input_dict')
input_dict
import pandas as pd
input_df = pd.DataFrame(input_dict)
input_df = pd.Series(input_dict)
input_df
input_df.index
input_df['a']['b']
get_ipython().magic('logstop')

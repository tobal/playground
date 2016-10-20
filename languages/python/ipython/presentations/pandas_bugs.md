
import pandas as pd
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df
   a  b
0  1  3
1  2  4


df['a']
   a
0  1
1  2


df['a'].loc[2] = 100
df['a']
     a
0    1
1    2
2  100


df
   a  b
0  1  3
1  2  4


df['a'].loc[1] = 200
df['a']
     a
0    1
1  200
2  100


df
   a  b
0  1  3
1  2  4


df['c'] = df['a'] + df['b']
df
   a  b    c
0  1  3    4
1  2  4  204


df['c']
     c
0    4
1  204

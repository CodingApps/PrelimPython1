import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import style
style.use('ggplot')

web_stats = {'Day' : [1,2,3,4,5,6],
             'Visitors' : [43,53,24,45,64,34],
             'Bounce_Rate':[65,72,62,64,544,66]}

df = pd.DataFrame(web_stats)

print(df)
print(df.head())
print(df.tail())
print(df.tail(2))


df2 = df.set_index('Day')
print(df2.head())

print(df2.Visitors.tolist())
print(np.array(df2.Visitors.tolist()))
print(np.array(df2[['Visitors', 'Bounce_Rate']]))

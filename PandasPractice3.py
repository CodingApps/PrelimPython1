import pandas as pd
df = pd.read_csv('hmarket1.csv')

print(df.head())
df.set_index('Date', inplace=True)
df.to_csv('hmarket2.csv')

df = pd.read_csv('hmarket2.csv')
df.set_index('Date', inplace=True)

df = pd.read_csv('hmarket2.csv', index_col=0)
print(df.head())

df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('hmarket4.csv')
df.to_csv('hmarket5.csv', header=False)

df = pd.read_csv('hmarket5.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())

df.to_html('example.html')

df=pd.read_csv('hmarket5.csv', names=['Date', 'Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI': 'NewName:77006_HPI'}, inplace=True)
print(df.head())



                
                 

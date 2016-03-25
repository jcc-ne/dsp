import pandas as pd

df = pd.read_csv('faculty.csv')
df2 = df.loc[:, [' email']]
df2.to_csv('email.csv', index=False, header=None)

#Naman , 12514798
import pandas as pd
import numpy as np
PATH = r'C:\Users\naman\Desktop\MTNL.CSV'
df   = pd.read_csv(PATH, parse_dates=['Year'])

x = df['Borrowings'].values
y = df['Total Assets'].values
r = np.corrcoef(x, y)[0, 1]

if r > 0.7:
    print('Debt-driven growth – REVIEW leverage')
elif r > 0.4:
    print('Moderate link – MONITOR borrowings')
else:
    print('Healthy – assets not debt-dependent')
print(f'Correlation = {r:.3f}')

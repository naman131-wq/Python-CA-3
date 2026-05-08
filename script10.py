# Naman, 12514798
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'C:\Users\naman\Desktop\MTNL.CSV'
df   = pd.read_csv(PATH, parse_dates=['Year'])

sns.histplot(df['Reserves'], kde=True,
             color='steelblue', bins=8)
plt.title('Distribution of Reserves')
plt.xlabel('Reserves (₹ Cr)')
plt.ylabel('Frequency')
plt.show()

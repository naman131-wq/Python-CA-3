# Naman , 12514798
import pandas as pd
import matplotlib.pyplot as plt
df   = pd.read_csv(r'C:\Users\naman\Desktop\MTNL.CSV', parse_dates=['Year'])
df.sort_values('Year', inplace=True)
plt.plot(df['Year'], df['Total Assets'],
         marker='o', color='teal')
plt.title('Tata Steel – Total Assets')
plt.xlabel('Year')
plt.ylabel('Total Assets (₹ Cr)')
plt.xticks(rotation=45)
plt.show()

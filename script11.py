#Naman , 12514798
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'C:\Users\naman\Desktop\MTNL.CSV'
df   = pd.read_csv(PATH, parse_dates=['Year'])

cols = ['Fixed Assets', 'Investments']
df_m = df[cols].melt(
    var_name='Type', value_name='Value')
sns.boxplot(x='Type', y='Value',
            data=df_m, palette='Set2')
plt.title('Fixed Assets vs Investments')
plt.show()

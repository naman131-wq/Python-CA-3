# Naman, 12514798
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
PATH = r'C:\Users\naman\Desktop\MTNL.CSV'
df   = pd.read_csv(PATH, parse_dates=['Year'])

df['TAD_Label'] = df['TAD'].map(
    {0: 'Low Deploy', 1: 'High Deploy'})
sns.countplot(x='TAD_Label', data=df,
              palette='coolwarm')
plt.title('Asset Deployment Category Count')
plt.ylabel('Number of Years')
plt.show()

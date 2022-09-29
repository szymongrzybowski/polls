import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('path/to/file/ur_cc.csv')

df.plot.scatter(x='United Right', y='Civic Coalition', title='Scatterplot of UR and CC results')
correlation = df.corr()
print(correlation)
plt.show()

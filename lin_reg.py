import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('path/to/file/spd_union.csv')
#print(df)
#table_shape = df.shape

#df.plot.scatter(x='SPD', y='Union', title='Scatterplot of SPD and Union results')
#correlation = df.corr()
#print(correlation)
#plt.show()

#correlation = df.corr()
#print(correlation)

X = df['SPD'].values.reshape(-1, 1)
y = df['Union'].values.reshape(-1, 1)

#print('x shape:', x.shape)
#print('x:', x)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

#print(x_train)
#print(y_train)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

union_score = regressor.predict(X)
print(union_score)

print(regressor.score(X_test, y_test))

stuff = len(union_score)
print(stuff)

plt.figure(figsize=(10, 6))
plt.title("Linear regression: SPD and Union", size=16)
plt.scatter(X, y)
plt.plot(X, union_score, c="red")
plt.show()

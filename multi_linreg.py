import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('path/to/file/all_parties.csv')

X = df[['Civic Coalition', 'The Left', 'Polish Coalition', 'Confederation', 'Poland 2050']].values
y = df['United Right'].values.reshape(-1, 1)
#print(X)
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_score = regressor.predict([[27.1, 9.0, 6.3, 5.6, 10.6]])
print(y_score)

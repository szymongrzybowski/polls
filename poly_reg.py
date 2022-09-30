import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('path/to/file/cc_tl.csv')

X = df['The Left'].values.reshape(-1, 1)
y = df['Civic Coalition'].values.reshape(-1, 1)

lin_reg = LinearRegression()
lin_reg.fit(X, y)

poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

lin_result = lin_reg.predict([[9.0]])
print(lin_result)

poly_result = lin_reg2.predict(poly_reg.fit_transform([[9.0]]))
print(poly_result)

plt.scatter(X, y, color='blue')
plt.plot(X, lin_reg.predict(X), color='red')
plt.title('Linear Regression')
plt.xlabel('TL')
plt.ylabel('CC')
plt.show()

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='blue')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color='red')
plt.title('Truth or bluff (Polynomial Regression)')
plt.xlabel('TL')
plt.ylabel('CC')
plt.show()

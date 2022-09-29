import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

df = pd.read_csv('C:/Users/SzymonG/Downloads/cc_tl.csv')

X = df['The Left'].values.reshape(-1,1)
y = df['Civic Coalition'].values.reshape(-1,1)

StdS_X = StandardScaler()
StdS_y = StandardScaler()
X_ = StdS_X.fit_transform(X)
y_ = StdS_y.fit_transform(y)

#plt.scatter(X_, y_, color = 'skyblue') 
#plt.title('Scatter Plot') 
#plt.xlabel('The Left') 
#plt.ylabel('Civic Coalition') 
#plt.show()

regressor = SVR(kernel = 'rbf')
regressor.fit(X_, y_.ravel())

a = regressor.predict(StdS_X.transform([[7]]))
#print(a)

a2 = a.reshape(-1,1)
#print(a2)

a3 = StdS_y.inverse_transform(a2)
print(a3)

plt.scatter(StdS_X.inverse_transform(X_), StdS_y.inverse_transform(y_), color = 'skyblue')
plt.plot(StdS_X.inverse_transform(X_), StdS_y.inverse_transform(regressor.predict(X_).reshape(-1,1)), color = 'red')
plt.title('Support Vector Regression Model')
plt.xlabel('The Left')
plt.ylabel('Civic Coalition')
plt.show()

# Scott McElfresh sme1d1 ICP5-3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data = pd.read_csv('data5.csv')
data = data.drop(['Id'], axis=1)

data2 = data
data2['City Group'] = data2['City Group'].astype('category')  # set City group to category d-type
data2['City Group'] = data2['City Group'].cat.codes  # use .cat accessor on City Group to generate numerical codes
# print(data['City Group'].head())
data2['Type'] = data2['Type'].astype('category')  # set Type to category d-type
data2['Type'] = data2['Type'].cat.codes  # use .cat accessor on Type to generate numerical codes
# print(data['Type'].head())
# print(data2.head())

# Compute the correlation
numeric_features = data2.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print(corr['revenue'].sort_values(ascending=False)[:6], '\n')
print(corr['revenue'].sort_values(ascending=False)[-6:])
# P2, P6, P28, P29 and City Group are highest correlated to revenue (positive and negative)

data3 = data2.filter(['P2', 'P6', 'P28', 'P29', 'City Group', 'revenue'])

# print(data3.head())
y = np.log(data3.revenue)  # log transform on our response variable
X = data3.drop(['revenue'], axis=1)  # remove response variable from dataset and 'no-correlation' data
# print(y.head())
# print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)  # create test and train sets

lr = linear_model.LinearRegression()  # use linear regression model
model = lr.fit(X_train, y_train)  # fit our data
y_pred = lr.predict(X_test)  # create our prediction data based off our test data
r2 = r2_score(y_test, y_pred)  # show r^2 score

# R^2 and RMSE

# print("R^2 is: {}\n".format(r2))  # negative = bad fit
# print("RMSE is: {}\n".format(mean_squared_error(y_test, y_pred)))  # high = bad fit

# Graph Data
plot1 = plt.figure(1)
actual_values = y_test
plt.scatter(y_pred, actual_values, alpha=.25, color='r')
plt.xlabel('Predicted Revenue')
plt.ylabel('Actual Revenue')
plt.title('Linear Regression 5-3')
plt.figtext(.5, .8, ('RMSE is: {}'.format(mean_squared_error(y_test, y_pred))))
plt.figtext(.5, .75, ('R^2 is: {}'.format(r2)))

mean = np.mean(y)
std = np.std(y)
threshold = 3
outlier = []
outindex = []
counter = 0

for i in y:
    z = (i - mean) / std
    if z > threshold:
        outlier.append(i)
        outindex.append(counter)
    counter += 1

g = np.array(X)
h = np.array(y)
t = np.delete(g, [outindex], 0)
u = np.delete(h, [outindex], 0)

X_train, X_test, y_train, y_test = train_test_split(t, u, random_state=42, test_size=.33)
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
r2 = r2_score(y_test, y_pred)

# Evaluate using R^2 and RMSE (Root Mean Square Error) - standard deviation of prediction errors

# print("R^2 is: {}\n".format(r2))  # negative = bad fit
# print('RMSE is: \n', mean_squared_error(y_test, y_pred))  # high = bad fit

# Graph data
plot2 = plt.figure(2)
actual_values = y_test
plt.scatter(y_pred, actual_values, alpha=.25, color='g')
plt.xlabel('Predicted Revenue')
plt.ylabel('Actual Revenue')
plt.title('Linear Regression 5-3 - Revenue outliers removed')
plt.figtext(.5, .8, ('RMSE is: {}'.format(mean_squared_error(y_test, y_pred))))
plt.figtext(.5, .75, ('R^2 is: {}'.format(r2)))
plt.show()

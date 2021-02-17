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
obj_data = data.select_dtypes(include='object').copy()
# print(obj_data.head())
data2 = data
data2['City Group'] = data2['City Group'].astype('category')  # set City group to category d-type
data2['City Group'] = data2['City Group'].cat.codes  # use .cat accessor on City Group to generate numerical codes
# print(data['City Group'].head())
data2['Type'] = data2['Type'].astype('category')  # set Type to category d-type
data2['Type'] = data2['Type'].cat.codes  # use .cat accessor on Type to generate numerical codes
# print(data['Type'].head())
# print(data2.head())
'''
# Compute the correlation matrix
corr = data2.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(240, 10, n=9)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr,  annot=True, fmt=".1", mask=mask, cmap=cmap, vmax=.4,
            square=False, linewidths=.5)
plt.show()
'''
# P2, P6, P21, P22, P28 are highest correlated to revenue
# X = data.drop(data.columns.difference(['P2','P6']), 1, inplace=True) #nope - doesn't work
data3 = data2.filter(['P2', 'P6', 'P21', 'P22', 'P28', 'revenue'])
print(data3.head())
y = np.log(data3.revenue)  # log transform on our response variable
X = data3.drop(['revenue'], axis=1)  # remove response variable from dataset and 'no-correlation' data
print(y.head())
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)  # create test and train sets

lr = linear_model.LinearRegression()  # use linear regression model
model = lr.fit(X_train, y_train)  # fit our data
y_pred = lr.predict(X_test)  # create our prediction data based off our test data
r2 = r2_score(y_test, y_pred)  # show r^2 score

##Evaluate the performance and visualize results

print("R^2 is: {}\n".format(r2))  # negative = bad fit
print("RMSE is: {}\n".format(mean_squared_error(y_test, y_pred)))  # high = bad fit

##visualize
plot1 = plt.figure(1)
actual_values = y_test
plt.scatter(y_pred, actual_values, alpha=.25, color='r')
plt.xlabel('Predicted Revenue')
plt.ylabel('Actual Revenue')
plt.title('Linear Regression Model 1')
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

print("R^2 is: {}\n".format(r2))  # negative = bad fit
print('RMSE is: \n', mean_squared_error(y_test, y_pred))  # high = bad fit

# Graph data
plot2 = plt.figure(2)
actual_values = y_test
plt.scatter(y_pred, actual_values, alpha=.25, color='b')
plt.xlabel('Predicted Revenue')
plt.ylabel('Actual Revenue')
plt.title('Linear Regression Model - Revenue outliers removed')
plt.figtext(.5, .8, ('RMSE is: {}'.format(mean_squared_error(y_test, y_pred))))
plt.figtext(.5, .75, ('R^2 is: {}'.format(r2)))
plt.show()


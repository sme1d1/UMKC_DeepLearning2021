# Scott McElfresh sme1d1 ICP5-1
"""
1.Delete all the outlier data for the GarageArea field
(for the same data set in the use case: House Prices).* for this task you need to plot
GarageArea field and SalePrice in scatter plot, then check which numbers are anomalies.
"""
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data set - dataframe
train = pd.read_csv('train5.csv')

# define x and y dataframes
x = train['GarageArea']
y = train['SalePrice']

# setup Z score
mean = np.mean(x)
std = np.std(x)
threshold = 3
outlier = []  # array for outliers
outindex = []  # array for outliers index to delete from both dataframes
counter = 0
for i in x: # Calculate Z-Score
    z = (i - mean) / std
    if z > threshold:
        outlier.append(i)
        outindex.append(counter)
    counter += 1

print('Outliers in Garage Area are', outlier)
print('Outlier indices are', outindex)

# plot scatter graph (no outlier deletion)
plot1 = plt.figure(1)
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.title("Garage Area vs Sale Price - ICP5")
plt.scatter(x, y, color='green', marker='.')

g = np.array(x)  # create new numpy arrays from x
h = np.array(y)  # create new numpy arrays from y
t = np.delete(g, [outindex], 0)  # delete outlier from g and h arrays
u = np.delete(h, [outindex], 0)

# plot scatter graph with outlier deletion
plot2 = plt.figure(2)
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.title("Garage Area vs Sale Price - Outliers Removed")
plt.scatter(t, u, color='blue', marker='.')

plt.show()

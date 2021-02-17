# Scott McElfresh sme1d1 ICP5-1
"""
1.Delete all the outlier data for the GarageArea field
(for the same data set in the use case: House Prices).* for this task you need to plot
GarageArea field and SalePrice in scatter plot, then check which numbers are anomalies.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
train = pd.read_csv('train5.csv')
x = train['GarageArea']
y = train['SalePrice']
mean = np.mean(x)
std = np.std(x)
threshold = 3
outlier = []
outindex = []
counter = 0
for i in x:
    z = (i - mean) / std
    if z > threshold:
        outlier.append(i)
        outindex.append(counter)
    counter += 1

print('Outliers in Garage Area are', outlier)
print('Outlier indices are', outindex)

# plot the full graph
plot1 = plt.figure(1)
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.title("Garage Area vs Sale Price - ICP5")
plt.scatter(x, y, color='green', marker='.')

g = np.array(x)
h = np.array(y)
t = np.delete(g, [outindex], 0)
u = np.delete(h, [outindex], 0)

plot2 = plt.figure(2)
plt.xlabel("Garage Area")
plt.ylabel("Sale Price")
plt.title("Garage Area vs Sale Price - Outliers Removed")
plt.scatter(t, u, color='blue', marker='.')

plt.show()

"""
Using NumPy create random vector of size 20 having only floats in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0(axis=1)
(you can NOT implement it via for loop)

Scott McElfresh sme1d1 Deep Learning 2021 2/3/2021
"""

import numpy as np

# create random array of size 20 with floats from 1 to 20
# reshape to a 4 x 5 array
a = np.random.uniform(1.0, 20.0, 20).reshape(4, 5)
print(a)
print("\n")
# find max values of a and return array of those values
b = np.max(a, axis=1, initial=0)
# compare values of a and b to create conditional True or False
c = np.in1d(a, b).reshape(4, 5)
# replace values in a, where c is True, to 0
d = np.where(c == True, 0.0, a)
# print new matrix of with zeros
print(d)

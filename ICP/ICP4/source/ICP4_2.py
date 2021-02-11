# Scott McElfresh sme1d1 ICP4_2
# Using Naive Bayes method

import pandas as pd
from sklearn.model_selection import train_test_split

# Import Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB

# For testing normal distribution
from scipy.stats import norm
from scipy import stats

# Import classification report
from sklearn.metrics import classification_report

# Import seaborn and plot
import seaborn as sns
import matplotlib.pyplot as plt

# read data csv
train = pd.read_csv("./glass.csv")

x = train.drop('Type', axis=1)
# print(x[0:9]) test
# print(x)
# define our test and train data
y = train['Type']
# print(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=90)

# create our model
model = GaussianNB()

# train the model
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# Model Accuracy
acc= round(model.score(x_train, y_train) * 100, 2)
print("Gaussian Naive Baylor accuracy is: ", acc)

print(classification_report(y_test, y_pred, zero_division=0))

x = norm.rvs(size=500)
shapiro_test = stats.shapiro(x)
print(shapiro_test)  # p>.05 a normal distribution


# Check data distribution

sns.set_theme()

sns.displot(data=train, x="Type")
plt.show()

# may be dependent features which cause NB to perform worse than SVM - NB assumes features are interdependent
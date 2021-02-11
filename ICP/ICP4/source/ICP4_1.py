# Scott McElfresh sme1d1 ICP4_1

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

train = pd.read_csv("./train_preprocessed.csv")

total = train['Sex'].count()
female = train['Sex'].sum()
print("Male: {}".format(total - female) + "| Female: {}".format(female))

print(train.corr(method='pearson'))

sns.catplot(x="Sex", y="Survived", hue="Pclass", kind="bar", data=train)
plt.show()
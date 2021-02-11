# Scott McElfresh sme1d1 ICP4_3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Import classification report
from sklearn.metrics import classification_report

train = pd.read_csv("./glass.csv")
x = train.drop('Type', axis=1)
y = train['Type']
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=90)

model = SVC(kernel='linear')

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
# print(y_pred)

# Model Accuracy
acc= round(model.score(x_train, y_train) * 100, 2)
print("SVC accuracy: ", acc)

print(classification_report(y_test, y_pred, zero_division=0))




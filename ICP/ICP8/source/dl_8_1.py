# Scott McElfresh sme1d1 Deep Learning Week 8

# import libraries and methods
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  # load scaler

dataset = pd.read_csv("diabetes.csv", header=None).values  # read data
dataset = pd.DataFrame(dataset)  # create data set
keepdata = dataset.loc[:, [0, 1, 2, 3, 4, 5, 6, 7]]  # specify data set columns
y = dataset.loc[:, 8]  # specify response variable
sc.fit(keepdata)  # fit data
datascaled = sc.transform(keepdata)  # perform standardization by centering and scaling
datascaled = pd.DataFrame(datascaled)  # create dataFrame from scaled data
# print(datascaled)
# print(y)

# create test and train datasets
X_train, X_test, Y_train, Y_test = train_test_split(datascaled, y,
                                                    test_size=0.25, random_state=87)

diabetes_nn = Sequential()  # create model
diabetes_nn.add(Dense(16, input_dim=8, activation='relu'))  # hidden layer
diabetes_nn.add(Dense(32, activation='relu'))  # hidden layer
diabetes_nn.add(Dense(4, activation='relu'))  # hidden layer
diabetes_nn.add(Dense(1, activation='sigmoid'))  # output layer
diabetes_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])  # create list of metrics
diabetes_nn_fitted = diabetes_nn.fit(X_train, Y_train, epochs=100, shuffle=True, validation_split=0.2,
                                     initial_epoch=0)  # train our model
print(diabetes_nn.summary()) # print summary
diabetes_nn.test_on_batch(X_test, Y_test)  # test model on batch of samples

# print(diabetes_nn_fitted.history.keys())
# Create plots for accuracy and loss
#  "Accuracy Plot"
plot1 = plt.figure(1)
plt.plot(diabetes_nn_fitted.history['acc'])
plt.plot(diabetes_nn_fitted.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')

# "Loss Plot"
plot3 = plt.figure(2)
plt.plot(diabetes_nn_fitted.history['loss'])
plt.plot(diabetes_nn_fitted.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

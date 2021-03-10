# Scott McElfresh sme1d1 Deep Learning Week 8

from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  # set scaler

bc = pd.read_csv("breastcancer.csv")  # read data
bc = pd.DataFrame(bc)  # create Dataframe from data
# print(list(bc.columns.values)) # see dataframe headers

# Determine Nulls
'''
nulls = pd.DataFrame(bc.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls.head())
# Get rid of Unnamed 32 - is filled with nulls
'''

# convert categorical data to numerical data
bc['diagnosis'] = bc['diagnosis'].astype('category')  # set diagnosis group to category d-type
bc['diagnosis'] = bc['diagnosis'].cat.codes  # use .cat accessor on diagnosis to generate numerical codes
y = bc['diagnosis']  # set response variable
# remove response variable from dataset, 'no-correlation', and Null data
bc = bc.drop(['diagnosis', 'id', 'Unnamed: 32'], axis=1)

sc.fit(bc)  # fit data
datascaled = sc.transform(bc)  # perform standardization by centering and scaling
datascaled = pd.DataFrame(datascaled)  # create DataFrame

# Unscalled data test/train set = loss: 0.1864 - acc: 0.9235
# X_train, X_test, Y_train, Y_test = train_test_split(bc, y, test_size=0.25, random_state=87)

# Scalled data test/train set = loss: -/ acc: 1.0000
X_train, X_test, Y_train, Y_test = train_test_split(datascaled, y,
                                                    test_size=0.25, random_state=87)
bc_nn = Sequential()  # create model
bc_nn.add(Dense(30, input_dim=30, activation='relu'))  # hidden layer
bc_nn.add(Dense(60, activation='relu'))  # hidden layer
bc_nn.add(Dense(15, activation='relu'))  # hidden layer
bc_nn.add(Dense(1, activation='sigmoid'))  # output layer
bc_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])  # create list of metrics
bc_nn_fitted = bc_nn.fit(X_train, Y_train, epochs=100,
                         initial_epoch=0, shuffle=True, validation_split=0.2)  # train model
print(bc_nn.summary())  # print summary
# Create plots for accuracy and loss
#  "Accuracy Plot"
plot1 = plt.figure(1)
plt.plot(bc_nn_fitted.history['acc'])
plt.plot(bc_nn_fitted.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='lower right')

# "Loss Plot"
plot3 = plt.figure(2)
plt.plot(bc_nn_fitted.history['loss'])
plt.plot(bc_nn_fitted.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.show()

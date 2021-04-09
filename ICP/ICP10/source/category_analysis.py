# ICP 10 - sme1d1 - Scott McElfresh part 3

from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.layers import Dropout
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(shuffle=True)
categories = ('sci.med', 'sci.space', 'alt.atheism', 'talk.religion.misc',
              'talk.politics.misc', 'soc.religion.christian')
remove = ('headers', 'footers', 'quotes')
train_data = fetch_20newsgroups(subset='train', categories=categories,
                                remove=remove, return_X_y=True)

test_data = fetch_20newsgroups(subset='test', categories=categories,
                               remove=remove, shuffle=True, random_state=42)

# print(train_data[0])
# print(train_data[1])
sentences = train_data[0]  # return_X_y gives us data and target
y = train_data[1]

# tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
# getting the vocabulary of data
sentences = tokenizer.texts_to_matrix(sentences)
# print(sentences)

X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)
training_set_shape = X_train.shape
print(training_set_shape)  # find our input dimension

# print(sentences.shape)
# Number of features
# print(input_dim)
dimensions = 300
V_X_Dim = dimensions * training_set_shape[1]
model = Sequential()
# our input dim is the V of [* X V] of our training set
model.add(layers.Dense(dimensions, input_dim=(training_set_shape[1]), activation='relu'))
# layer size is words * units, VxN, : activation is softmax
model.add(layers.Dense(V_X_Dim, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=15, verbose=True, validation_data=(X_test, y_test), batch_size=64)
# print((history.history.keys()))  #  determine history keys for plots

# Plot accuracy
plot2 = plt.figure(2)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='lower right')

# "Loss Plot"
plot3 = plt.figure(3)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

# ICP 10 - sme1d1 - Scott McElfresh

from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.layers import Dropout

df = pd.read_csv('imdb_master.csv', encoding='latin-1')
#print(df.head())

sentences = df['review'].values
y = df['label'].values
#print(sentences)
#print(y)

# tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
# getting the vocabulary of data
sentences = tokenizer.texts_to_matrix(sentences)

le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)
training_set_shape = X_train.shape
print(training_set_shape)  # find our input dimension

# print(sentences.shape)
# Number of features
# print(input_dim)
model = Sequential()
# our input dim is the V of [* X V] of our training set (2000)
model.add(layers.Dense(300, input_dim=(training_set_shape[1]), activation='relu'))
model.add(Dropout(0.2))  # trying to remove some over-fitting on model
model.add(layers.Dense(600, activation='relu'))
model.add(Dropout(0.2))

# layer size is words * units, VxN, (300 * 2000 = 60000) : activation is softmax
model.add(layers.Dense(60000, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(X_train, y_train, epochs=5, verbose=True, validation_data=(X_test, y_test), batch_size=64)
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

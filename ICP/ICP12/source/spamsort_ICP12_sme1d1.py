# Scott McElfresh sme1d1 ICP 12

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import load_model
import re
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

tf.random.set_seed(42)  # tensorflow seed fixing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('spam.csv')
# Keeping only the neccessary columns
data = data[['v2', 'v1']]
data['v2'] = data['v2'].apply(lambda x: x.lower())
data['v2'] = data['v2'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))
data['v2'] = data['v2'].apply((lambda x: re.sub('\S*@\S*\s?', '', x)))
data['v2'] = data['v2'].apply((lambda x: re.sub('\s+', ' ', x)))

for idx, row in data.iterrows():
    row[0] = row[0].replace('rt', ' ')

print("Number of ham samples: ")
print(data[data['v1'] == 'ham'].size)
print("Number of spam samples: ")
print(data[data['v1'] == 'spam'].size)


max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['v2'].values)
X = tokenizer.texts_to_sequences(data['v2'].values)
X = pad_sequences(X)

labelencoder = LabelEncoder()
integer_encoded = labelencoder.fit_transform(data['v1'])
y = to_categorical(integer_encoded)
embed_dim = 128
lstm_out = 196


def createmodel():
    model = Sequential()
    model.add(Embedding(max_features, embed_dim, input_length=X.shape[1]))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(2, activation='sigmoid'))
    model.compile(loss=tf.losses.categorical_crossentropy, optimizer='adam', metrics=['accuracy'])

    return model

#model = createmodel()
#print(model.summary())
epochs = 3
batch_size = 20

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=False)
#history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=epochs, batch_size=batch_size)
model = load_model('ICP12spam_model.h5')
score, acc = model.evaluate(X_test, Y_test, verbose=2, batch_size=batch_size)

#model.save('ICP12spam_model.h5')

#  GridSearchCV - takes a long time to run. On source it resulted in batch size: 10, epochs: 2
'''
model = KerasClassifier(build_fn=createmodel, verbose=2)
batch_size = [10, 20, 40]
epochs = [2, 3]
param_grid = dict(batch_size=batch_size, epochs=epochs)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
grid_result = grid.fit(X_train, Y_train)
# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
'''

newtext = ['WINNER!! As a valued network customer you have been selected to receivea �900 prize reward! '
           'To claim call 09061701461. Claim code KL341. Valid 12 hours only.']
print(newtext)
# newtext = ['Hi Mom, please give me a call']
newtext = tokenizer.texts_to_sequences(newtext)
newtext = pad_sequences(newtext, maxlen=152, dtype='int32', value=0)
sentiment = model.predict(newtext, batch_size=1, verbose=2)[0]

print("Predictions\n ")

print("HAM: [1,0], SPAM: [0,1]")
print(sentiment)
if sentiment[0] > sentiment[1]:
    print("Ham prediction")
else:
    print("Spam prediction")


# Accuracy Plot
'''
plot2 = plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
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
'''
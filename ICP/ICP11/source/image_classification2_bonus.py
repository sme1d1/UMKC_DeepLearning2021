# Simple CNN model for CIFAR-10
# Scott McElfresh sme1d1 4/12/2021 bonus

import numpy
from keras.datasets import cifar10
from keras.utils import np_utils
from keras import backend as K
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

K.set_image_data_format('channels_last')

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
# normalize inputs from 0-255 to 0.0-1.0
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train / 255.0
X_test = X_test / 255.0
# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# load our model
model = load_model('cifar10_model.h5')
# evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))

# print categories
print("Categories: 0: airplane, 1: automobile, 2: bird, 3: cat, 4: deer, 5: dog, 6: frog, 7: horse, 8: ship, 9: truck")

# create array of predicted categories
result = np.argmax(model.predict(X_test), axis=-1)

labelsAndTrainingImages = list(zip(X_test, y_test))
# plot images and their labels
for index, (image, label) in enumerate(labelsAndTrainingImages[:6]):
    plt.subplot(2, 3, index + 1)
    plt.imshow(image, interpolation='nearest')
    plt.title("Label " + '%i' % result[index])
plt.show()

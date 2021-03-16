from keras import Sequential
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# print(train_images.shape[1:])
# process the data
# 1. convert each image of shape 28*28 to 784 dimensional which will be fed to the network as a single feature
dimData = np.prod(train_images.shape[1:])
# print(dimData)
train_data = train_images.reshape(train_images.shape[0], dimData)
test_data = test_images.reshape(test_images.shape[0], dimData)

# convert data to float and scale values between 0 and 1
train_data = train_data.astype('float')
test_data = test_data.astype('float')
# scale data
train_data /= 255.0
test_data /= 255.0
# change the labels from integer to one-hot encoding. to_categorical is doing the same thing as LabelEncoder()
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

# creating network
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(10, activation='softmax'))
# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Create validation set
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=8, verbose=2,
                    validation_data=(test_data, test_labels_one_hot))
# print((history.history.keys()))

# evaluate model's error
score = model.evaluate(test_data, test_labels_one_hot, verbose=0)
print("Baseline error: %.2f%%" % (100 - score[1] * 100))

# Plot a single image, its label, and inference (model prediction for label)
infer = str(np.argmax(model.predict(test_data[0].reshape(1, 784))))
labelsAndTrainingImages = list(zip(test_images, test_labels))

plot4 = plt.figure(4)
plt.axis('off')
plt.imshow(test_images[0], cmap='gray', interpolation='nearest', aspect='equal')
plt.title("Label " + str(test_labels[0]) + "\n" + "Infer " + infer)

# Plot first twenty images, labels, and inference
plot1 = plt.figure(figsize=(10, 10))
for index, (image, label) in enumerate(labelsAndTrainingImages[:20]):
    plt.subplot(4, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap='gray', interpolation='nearest', aspect='equal')
    plt.title("Label " + '%i' % label + "\n" + "Infer " +
              str(np.argmax(model.predict(test_data[index].reshape(1, 784)))))

# Plot accuracy
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

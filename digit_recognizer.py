# TensorFlow handwritten digit analysis
#
#
# Written by Ryan Monaghan Jr. for the purpose of demonstrating a real world application
# of a machine learning algorithm for identifying/digitizing handwritten digits.
#
# March 13th, 2019
#
# Works with all keras datasets


from __future__ import absolute_import, division, print_function

# import tensorflow and keras datasets
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print("Using Tensorflow version", tf.__version__)

# Define dataset to be used
mnist_dataset = keras.datasets.mnist

# Parse the dataset
(train_images, train_labels), (test_images, test_labels) = mnist_dataset.load_data()

# Define labels
class_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Scale and then divide by 255
train_images = train_images / 255.0

test_images = test_images / 255.0

# Define layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(train_images, train_labels, epochs=10) # Although this is enough, you can change the epochs here

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)

predictions = model.predict(test_images)


#  Plotting functions for displaying after the model is trained
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_labels[predicted_label], 100 * np.max(predictions_array), class_labels[true_label]), color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
plt.show()
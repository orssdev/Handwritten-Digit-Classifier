import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train[1])

# plt.figure()
# plt.imshow(x_test[0], cmap='gray')
# plt.colorbar()
# plt.grid(False)
# plt.show()

# Normalize the images to a range of 0 to 1 before feeding them to the neural network
x_train = x_train / 255.0
x_test = x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # input layer
    tf.keras.layers.Dense(512, activation='relu'),  # hidden layer
    tf.keras.layers.Dropout(0.3),                   # dropout layer to prevent overfitting
    tf.keras.layers.Dense(256, activation='relu'),  # hidden layer
    tf.keras.layers.Dropout(0.3),                   # dropout layer to prevent overfitting
    tf.keras.layers.Dense(10, activation='softmax')  # output layer
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20)  # train the model
model.evaluate(x_test, y_test)  # evaluate the model

model.save('testModel.h5')
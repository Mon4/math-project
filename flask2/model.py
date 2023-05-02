import tensorflow as tf
from keras.datasets import mnist
import pickle
from mnist import read_mnist_modified


def model(x_train, y_train, x_test, y_test):
    # normalization color values from 0-255 to 0-1
    x_train = x_train / 255.0,
    x_test = x_test / 255.0

    # Flattening is converting the data into a 1-dimensional array
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(784, activation='relu'),
      tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20, batch_size=200)

    model.save("myModel")

    with open('./trainHistory.pkl', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)


# (x_train, y_train), (x_test, y_test) = mnist.load_data()
X_train, Y_train, X_test, Y_test = read_mnist_modified()
model(X_train, Y_train, X_test, Y_test)

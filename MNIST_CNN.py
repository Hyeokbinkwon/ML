import numpy as np
import tensorflow as tf
import random

mnist = tf.keras.datasets.mnist

########### Data Set. 자체가 2 그룹으로 나누어져 있음 ##############
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test = x_test /255

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


y_train = tf.keras.utils.to_categorical(y_train,10)
y_test = tf.keras.utils.to_categorical(y_test,10)

learning_rate = 0.001
training_epochs = 12
batch_size = 128

tf.model = tf.keras.Sequential()

tf.model.add(tf.keras.layers.Conv2D(filters=24, kernel_size=(3,3), input_shape=(28,28,1),activation='relu'))
tf.model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))

tf.model.add(tf.keras.layers.Flatten())
tf.model.add(tf.keras.layers.Dense(units=10, kernel_initializer='glorot_normal',activation='softmax'))

tf.model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=learning_rate),metrics=['accuracy'])
tf.model.fit(x_train, y_train, batch_size=batch_size, epochs=training_epochs)

y_predicted = tf.model.predict(x_test)
for x in range(0, 10):
    random_index = random.randint(0, x_test.shape[0]-1)
    print("index: ", random_index,
          "actual y: ", np.argmax(y_test[random_index]),
          "predicted y: ", np.argmax(y_predicted[random_index]))

evaluation = tf.model.evaluate(x_test, y_test)
print('loss: ', evaluation[0])
print('accuracy', evaluation[1])
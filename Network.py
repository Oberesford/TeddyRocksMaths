import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1) #Normalising our data
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))#Input layer
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))#2 Hidden layers with 128 Neurons 
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

loss,accuracy = model.evaluate(x_test, y_test)
print(f"Accuracy:{accuracy}")
print(f"Loss:{loss}")
model.save("digits.model")

for x in range(1,6):
    img = cv.imread(f'{x}.png')[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print(np.argmax(prediction))
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()

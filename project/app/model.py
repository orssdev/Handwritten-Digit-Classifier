import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model

model = load_model('testModel.h5')

probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

image = Image.open('8.png').convert("L")

print(image.size)
def image_preprocessing(image):
    size = (28, 28)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalize_array = (image_array.astype(np.float32) / 255.0) - 1
    data = np.expand_dims(normalize_array, axis=(0, -1))  # shape becomes (1, 28, 28, 1)
    return data

image = image_preprocessing(image)

predictions = probability_model(image)

# print(predictions[0])

def get_prediction(predictions):
    confidence = 0
    for i in range(10):
        if (predictions)[i] > confidence:
            confidence = predictions[i]
            number = i

    return (number, round(float(confidence),3))

n = (get_prediction(predictions[0]))[0]     # predicted number
c = (get_prediction(predictions[0]))[1]     # confidence
print("Predicted number of "+str(n)+" with a confidence of " +str(c * 100) + "%")


import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

model = load_model('testModel.h5')

probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

image = Image.open('numbers/9.png').convert("L")
inverted_image = ImageOps.invert(image)

def image_preprocessing(image):
    size = (28, 28)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image).astype(np.uint8)

    threshold = 100
    image_array = np.where(image_array > threshold, 255, 0)

    normalize_array = (image_array.astype(np.float32) / 255.0)
    data = np.expand_dims(normalize_array, axis=(0, -1))  # shape becomes (1, 28, 28, 1)
    return data

img = image_preprocessing(inverted_image)

# plt.imshow(img[0, :, :, 0], cmap='gray')
# plt.title("Processed Input")
# plt.show()

predictions = probability_model(img)

print(predictions[0])

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


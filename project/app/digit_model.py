import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
from io import BytesIO


def image_preprocessing(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert("L")
    image = ImageOps.invert(image)
    size = (28, 28)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image).astype(np.uint8)

    # threshold = 30
    # image_array = np.where(image_array > threshold, 255, 0)

    normalize_array = (image_array.astype(np.float32) / 255.0)
    data = np.expand_dims(normalize_array, axis=(0, -1))  # shape becomes (1, 28, 28, 1)
    return data

def predict_digit(image_bytes):
    model = load_model('app/Digitron.h5')
    # probability_model = tf.keras.Sequential([
    #     model,
    #     tf.keras.layers.Softmax()
    # ])

    img = image_preprocessing(image_bytes)

    # UNCOMMENT FOR IMAGE PREVIEW
    # plt.imshow(img[0, :, :, 0], cmap='gray')
    # plt.title("Processed Input")
    # plt.show()

    predictions = model(img)
    # print("Predictions array:\n", predictions.numpy())
    confidence = 0
    for i in range(10):
        if (predictions[0][i] > confidence):
            confidence = predictions[0][i]
            number = i
    #confidences = predictions[0].numpy()
    #predicted_digit = int(np.argmax(confidences))
    confidence = round(float(confidence) * 100, 2)

    return {
        "digit": number,
        "confidence": confidence
    }
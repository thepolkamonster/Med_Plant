import numpy as np
import tensorflow 
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

#model = tensorflow.keras.models.load_model("plant_identification_model2.keras")

def predict(image_path, model):
    image = load_img(image_path, target_size=(224, 224))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    preprocessed_image = preprocess_input(image_array)
    predictions = model.predict(preprocessed_image)
    predicted_label_index = np.argmax(predictions)
    return predicted_label_index


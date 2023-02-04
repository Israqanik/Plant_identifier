import tensorflow as tf
import os
import numpy as np
from tensorflow.keras import layers
from PIL import Image
from skimage import transform
from tensorflow.keras.models import load_model
import pathlib


# finally solved , you have to set the name as -> saved_model.h5  
# also connect to jupyter, maybe that helps? actually it doesn't, it's stupid to think like that

model_path ="./saved_model.h5"

#print(model_path)
new_model = load_model(model_path)
new_model.summary()

def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (100, 100, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

image = load('jackdo.jpg')

x = new_model.predict(image)
y = np.argmax(x)
print(y)

# just to see the prediction destribution 
print(x)

classes = ['bay','coconut','jackfruit','mango','taro']
print("The detected class is", classes[y])

# as we took 100*100 images it's not giving good result , so increase the IMG_SHAPE = 256

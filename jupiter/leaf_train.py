# %%
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import matplotlib.pyplot as plt
import numpy as np
import glob
import shutil
import time
from tensorflow.keras import layers

# %%
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# %%
pwd

# %%
base_dir =os.path.join('C:\\Users\\ASUS\\Jupyter Files Python\\leaf')

# %%
classes = ['bay','coconut','jackfruit','mango','taro']

# %%
for c1 in classes:
  img_path = os.path.join(base_dir, c1)
  images = glob.glob(img_path + '/*.jpg') # import glob
  print(f"{c1} : {len(images)} images")
  train, val = images[:round(len(images)*0.8)], images[round(len(images)*0.8):]

  for t in train:
    if not os.path.exists(os.path.join(base_dir,'train', c1)):
      os.makedirs(os.path.join(base_dir, 'train', c1))
    shutil.move(t, os.path.join(base_dir, 'train', c1)) # import shutil

  for v in val:
    if not os.path.exists(os.path.join(base_dir, 'val', c1)):
      os.makedirs(os.path.join(base_dir, 'val', c1))
    shutil.move(v, os.path.join(base_dir, 'val', c1))

# %%
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# %%
BATCH_SIZE = 20
IMG_SHAPE = 100

# %%
def plotImages(images_arr):
  fig, axes = plt.subplots(1,5,figsize=(20,20))
  axes = axes.flatten()
  for img, ax in zip(images_arr, axes):
    ax.imshow(img)
  plt.tight_layout()
  plt.show()

# %%
image_gen = ImageDataGenerator(rescale=1./255)

train_data_gen = image_gen.flow_from_directory(batch_size = BATCH_SIZE,
                                               directory= train_dir,
                                               shuffle= True,
                                               target_size =(IMG_SHAPE,IMG_SHAPE))

# %%
augmented_data =[train_data_gen[0][0][0] for i in range(5)]
plotImages(augmented_data)

# %%
sample_training_images, _=next(train_data_gen)
plotImages(sample_training_images[:5])

# %%
train_image_generator= ImageDataGenerator(rescale=1./255,
                                          rotation_range=45,
                                          width_shift_range=.15,
                                          height_shift_range=.15,
                                          horizontal_flip=True,
                                          zoom_range=0.5
                                          )

validation_image_generator = ImageDataGenerator(rescale=1./255)

# %%
train_data_gen =train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                          directory= train_dir,
                                                          shuffle= True,
                                                          target_size =(IMG_SHAPE,IMG_SHAPE),
                                                          class_mode='sparse')


# %%
val_data_gen = validation_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                             directory= val_dir,
                                                             shuffle= False,
                                                             target_size= (IMG_SHAPE,IMG_SHAPE),
                                                             class_mode='sparse')

# %%
model = tf.keras.Sequential([
                             tf.keras.layers.Conv2D(32, (3,3), activation = 'relu', input_shape= (IMG_SHAPE,IMG_SHAPE,3)),
                             tf.keras.layers.MaxPooling2D(2,2),

                             tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
                             tf.keras.layers.MaxPooling2D(2,2),
                             
                             tf.keras.layers.Conv2D(128,(3,3), activation='relu'),
                             tf.keras.layers.MaxPooling2D(2,2),

                             tf.keras.layers.Conv2D(128,(3,3), activation='relu'),
                             tf.keras.layers.MaxPooling2D(2,2),

                             tf.keras.layers.Flatten(),
                             tf.keras.layers.Dropout(0.2),
                             tf.keras.layers.Dense(512, activation='relu'),

                             tf.keras.layers.Dropout(0.2),
                             tf.keras.layers.Dense(5)
])

# %%
model.compile(optimizer='adam', 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# %%
model.summary()

# %%
EPOCHS = 15
history = model.fit_generator(
    train_data_gen,
    steps_per_epoch = int(np.ceil(train_data_gen.n/float(BATCH_SIZE))),
    epochs = EPOCHS,
    validation_data = val_data_gen,
    validation_steps = int(np.ceil(val_data_gen.n/float(BATCH_SIZE)))
)


# %%
# visualizing result
# variables
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss =history.history['val_loss']

epochs_range = range(EPOCHS)

# plotting accuracy
plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='validation Accuracy')
plt.legend(loc='lower right') # legend is used to indicate the location of text in graph
plt.title('Training and Validation Accuracy')

# plotting loss
plt.subplot(1,2,2)
plt.plot(epochs_range, loss, label ='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.savefig('./foo.png')
plt.show()

# %%
#saving the model
export_path_keras ="./leaves_v6_saved.h5"
print(export_path_keras)
model.save(export_path_keras)

# %%


# %%

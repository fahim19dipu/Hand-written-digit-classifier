
from __future__ import absolute_import,division,print_function

import tensorflow as tf
from keras import regularizers
import tensorflow_datasets as tfds
tf.logging.set_verbosity(tf.logging.ERROR)

import math
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
#from matplotlib import pyplot as plt


import tqdm
import tqdm.auto
tqdm.tqdm = tqdm.auto.tqdm

#print(tf.__version__)

tf.enable_eager_execution()

dataset,metadata = tfds.load('mnist', as_supervised=True , with_info = True)
train_dataset,test_dataset = dataset['train'],dataset['test']

class_names = ['0', '1', '2' ,'3', '4', 
               '5', '6', '7', '8', '9']


num_train_examples = metadata.splits['train'].num_examples
num_test_examples = metadata.splits['test'].num_examples

def normalize(images,labels):
  images = tf.cast(images,tf.float32)
  images /=255
  return images,labels
train_dataset = train_dataset.map(normalize)
test_dataset = test_dataset.map(normalize)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), padding='same', activation=tf.nn.relu,input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2), strides=2),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D((2, 2), strides=2),
    tf.keras.layers.Flatten(),    
    tf.keras.layers.Dense(128, activation=tf.nn.relu,kernel_regularizer=regularizers.l2(0.001)),
    tf.keras.layers.Dense(10,  activation=tf.nn.softmax)
])

model.compile(tf.train.AdamOptimizer(learning_rate=0.001),
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

BATCH_SIZE = 32
train_dataset = train_dataset.repeat().shuffle(num_train_examples).batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)


history = model.fit(train_dataset, epochs=5 ,steps_per_epoch=math.ceil(num_train_examples/BATCH_SIZE))
#model.fit(train_dataset, epochs=5 ,steps_per_epoch=math.ceil(num_train_examples/BATCH_SIZE),validation_split = 0.2)

test_loss, test_accuracy =model.evaluate(test_dataset,steps = math.ceil(num_test_examples/32))
print("Accuracy on test dataset : ",test_accuracy)

model.summary()

from keras.models import model_from_json
import os
# Save the model
model.save('path_to_my_model.h5')
model.save('same_one.model')
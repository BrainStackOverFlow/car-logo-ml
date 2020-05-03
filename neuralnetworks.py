from globalvars import img_width, img_height, img_colors

from utils import count_imgs_in_dataset

import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import Input, Dropout, Concatenate
from keras.layers import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.initializers import VarianceScaling
from keras.layers import Dropout
from keras.models import Model
from keras.layers import Input
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D

from sort import class_names

import numpy

import matplotlib.pyplot as plt

training_divide = 32
training_rounds = 5

""" print statics of the 

Arguments

Returns: 
	nothing
"""
def print_fit_statistics(history):
	for key in history.history.keys():
		plt.plot(history.history[key], label=key)
		plt.legend()
		plt.show()

def define_model():
	model = Sequential()
	model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(img_width,img_height,img_colors)))
	model.add(Conv2D(64, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(len(class_names), activation='softmax'))
	model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
	
	model.summary()
	
	return model

def train_model(model, train_dir: str, test_dir: str):
	datagen = ImageDataGenerator(rescale=1.0/255.0)
	
	train_generator = datagen.flow_from_directory(train_dir, class_mode='categorical', batch_size=int(count_imgs_in_dataset(train_dir)/training_divide) , target_size=(img_width,img_height), color_mode='rgb', shuffle=True)
	test_generator  = datagen.flow_from_directory(test_dir, class_mode='categorical', batch_size=int(count_imgs_in_dataset(test_dir)), target_size=(img_width,img_height), color_mode='rgb', shuffle=True)

	history = model.fit_generator(train_generator, steps_per_epoch=len(train_generator), validation_data=test_generator, validation_steps=len(test_generator), epochs=training_divide*training_rounds, verbose=2)

	print_fit_statistics(history)
	
def single_prediction(model, img):
	predictions = model.predict(numpy.array([numpy.array(img)]))
	return predictions[0]

from globalvars import debug_data, train_dir, test_dir, all_dir, model_weights_file_name, images_dir_path, dataset_path, images_zip_path, main_root_dir, img_width, img_height, class_names
from neuralnetworks import  define_model, train_model, single_prediction, training_divide
from sort import sort_all_dirs
from utils import get_file_path, extract_zip, load_photo, get_bool, print_prediction, count_imgs_in_dataset

from shutil import rmtree
import os

import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

# this files contains all teh ui options

""" trains the model and saves it

Args:
	model: the model object

Returns:
	nothing

"""
def ui_train_model(model):
	train_model(model, train_dir, test_dir)	
		
	if debug_data: print("finished trainig model...")
	
	if debug_data: print("saving model weights to disk...")
	
	model.save(model_weights_file_name)	

""" load the weights to the model from a file

Args:
	model: the model

Returns:
	nothing

"""
def ui_load_model(model):
	model.load_weights(model_weights_file_name)
	if debug_data: print("model loaded")

""" makes a prediction about one image

Args:
	the model object

Returns:
	nothing

"""
def ui_predict_img(model):
	print("enter an image path:")
	img_path = get_file_path()
	
	img = load_photo(img_path, img_width, img_height)
	prediction = single_prediction(model, img)
	
	print_prediction(img, prediction, class_names)


""" test the precision of the model when checking the training, test, training+test images group

Args:
	the model object

Returns:
	nothing

"""
def ui_test_precision(model):
	
	datagen = ImageDataGenerator(rescale=1.0/255.0)
	
	if debug_data: print("evaluating training data")

	train_generator = datagen.flow_from_directory(train_dir, class_mode='categorical', batch_size=int(count_imgs_in_dataset(train_dir)/training_divide) , target_size=(img_width,img_height), color_mode='rgb', shuffle=True)
	train_eval = model.evaluate_generator(train_generator, steps=count_imgs_in_dataset(train_dir),verbose = 1)

	if debug_data: print("evaluating test data")

	test_generator  = datagen.flow_from_directory(test_dir, class_mode='categorical', batch_size=count_imgs_in_dataset(test_dir), target_size=(img_width,img_height), color_mode='rgb', shuffle=True)
	test_eval = model.evaluate_generator(test_generator, steps=count_imgs_in_dataset(test_dir), verbose = 1)

	if debug_data: print("evaluating all data")

	all_generator = datagen.flow_from_directory(all_dir, class_mode='categorical', batch_size=int(count_imgs_in_dataset(all_dir)/training_divide), target_size=(img_width,img_height), color_mode='rgb', shuffle=True)
	all_eval = model.evaluate_generator(all_generator, steps=count_imgs_in_dataset(all_dir), verbose = 1)

	print("train images evaluation: loss=" + str(train_eval[0]) +", accuracy=" + str(train_eval[1]))
	print("test images evaluation: loss=" + str(test_eval[0]) +", accuracy=" + str(test_eval[1]))
	print("all images evaluation: loss=" + str(all_eval[0]) +", accuracy=" + str(all_eval[1]))


""" unzip the images and sort them to the correct folders

Args:
	the model object

Returns:
	nothing

"""
def ui_setup_env(model):
	try:
		os.mkdir(images_dir_path)
	except FileExistsError:
		pass
		
	if debug_data: print("extracting the zip file with all images...")
		
	extract_zip(images_zip_path, main_root_dir)
		
	if debug_data: print("finished extractin zip file")
		
	if debug_data: print("organzing the data set...")
		
	sort_all_dirs(dataset_path , images_dir_path)
		
	if debug_data: print("finished organzing the data set")

""" cleans all the files the program has created

Args:
	the model object

Returns:
	nothing

"""
def ui_clean_env(model):

	if debug_data: print("started cleaning the files the program generated")

	try:
		os.remove(model_weights_file_name)
	except FileNotFoundError: pass
	try:
		rmtree(images_dir_path)
	except FileNotFoundError: pass
	try:
		rmtree(dataset_path)
	except FileNotFoundError: pass

	if debug_data: print("finished cleaning")
	
# descrption of the functions + the functions into an easily accessible list
actions_strings = ["train the model", "load model", "make a prediction about an image", "test precision- check the precision of the model on all data", "set up enviornment - unzip and sort all the training images", "clear enviornment - delete all files this program generates", "exit"]
action_functions = [ui_train_model, ui_load_model, ui_predict_img, ui_test_precision, ui_setup_env, ui_clean_env]
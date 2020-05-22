#!/usr/bin/env python3

from sort import class_names
import utils
import os

# if true, the programs prints more data
debug_data = True



# the path to the root directory of this project 
main_root_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))


# file name of the model weights
model_weights_file_name = "casrnn_model.h5"

# the path to the model weigjts file
model_weights_path = utils.build_path([main_root_dir, model_weights_file_name])


# the path to the images zip file
images_zip_path = utils.build_path([main_root_dir, "images.zip"])

# the path to the images directory
images_dir_path = utils.build_path([main_root_dir, "images"])


# the path of the dataset directory
dataset_path = utils.build_path([main_root_dir, "dataset"])

# paths to the training + testing + all sorted images directories
train_dir = utils.build_path([dataset_path, "train"])
test_dir = utils.build_path([dataset_path, "test"])
all_dir = utils.build_path([dataset_path, "all"])


# setting file file path
path_vars_file_name = "path_vars.txt"



# width and height of the images that the model can understand
img_width = 50
img_height = 50

#how many color channels (3 = rgb images)
img_colors = 3



# names of the types of car logos
class_names = class_names
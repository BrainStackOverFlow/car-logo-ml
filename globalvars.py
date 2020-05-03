from sort import class_names
import utils
import os

debug_data = True

path_vars_file_name = "path_vars.txt"

model_weights_file_name = "casrnn_model.h5"

# the path to the root directory of this project 
main_root_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))

# the path to the model weigjts file
model_weights_path = utils.build_path([main_root_dir, model_weights_file_name])

images_zip_path = utils.build_path([main_root_dir, "images.zip"])
images_dir_path = utils.build_path([main_root_dir, "images"])

dataset_path = utils.build_path([main_root_dir, "dataset"])


train_dir = utils.build_path([dataset_path, "train"])
test_dir = utils.build_path([dataset_path, "test"])
all_dir = utils.build_path([dataset_path, "all"])

img_width = 50
img_height = 50
img_colors = 3

class_names = class_names
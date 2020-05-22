import numpy
from PIL import Image
import matplotlib.pyplot as plt

from re import match
import os
from os import listdir
import os.path
from os.path import isdir, isfile, join
from zipfile import ZipFile
from zipfile import is_zipfile
import shutil

""" check if a string s represents an integer number 

Args:
    s (string): string that will be checked

Returns:
    boolean: returns true if the strign represents an integer, else return false
"""
def RepresentsInt(s: str):
    return match(r"[-+]?\d+$", s) is not None

""" input an integer number in range

Args:
    range (tuple(int, int): the range of inputted integer

Returns:
    int: the integer inputted
"""
def get_integer(range: tuple) -> int:
	if len(range) is not 2:
		return False

	while True:
		print("enter an integer number in the range [" + str(range[0]) + ", " + str(range[1]) + "]")
		inp = input()
		
		if not RepresentsInt(inp):
			print("input is not an integer")
			continue
		
		if	int(inp) < range[0] or int(inp) > range[1]:
			print("integer inpuuted is out of range")
			continue
		
		return int(inp)


""" check if a string s represents a boolean 

Args:
    s (string): string that will be checked

Returns:
    boolean: returns true if the strign represents a boolean, else return false
"""
def RepresentsBool(s: str):
	if s in ["true", "t", "false", "f"]:
		return True
	return False

""" return the boolean value of a string

Args:
    s (string): string that will be checked

Returns:
    boolean: returns true if the string is "true" or "t", return false if the string is "false" or "f", else return None
"""
def GetBool(s: str):
	if s in ["true", "t"]: 
		return True
	if s in ["false", "f"]:
		return False
	return None

""" input an boolean

Args:
	no argumets

Returns:
    bool: returns a boolean value that was inputted by the user
"""
def get_bool() -> bool:
	while True:
		print("enter a boolean value:")
		print("for true value write: true, t")
		print("for false value write: false, f")
		
		inp = input()
		
		if not RepresentsBool(inp):
			print("input is not  boolean")
			continue
		
		return GetBool(inp)

""" input a file path

Args: none

Returns:
    str
"""
def get_file_path() -> str:
	while True:
		print("enter file path:")
		inp = input()
		if inp[0] == '"' and inp[-1] == '"':
			inp = inp[1:-1]
		
		if isfile(inp): break
		
		print('"' +  inp + '"' + ' is not a file')

	return inp

""" input a directory path

Args: none

Returns:
    str
"""
def get_dir_path() -> str:
	while True:
		print("enter directory path:")
		inp = input()
		
		if not isdir(inp):
			print("input is not an directory")
			continue
		
		return inp

""" extract a zip file

Args:
    zip_file_path (str): the path to the zip file
	extract_dir (str): the directory to extract the zip into

Returns:
    bool: true if extracted, false if not
"""
def extract_zip(zip_file_path: str, extract_dir: str) -> bool:
	if not isfile(zip_file_path):
		print("path: '" + zip_file_path + "' isnt a file")
		return False
	
	if not is_zipfile(zip_file_path):
		print("file: '" + zip_file_path + "' isnt a zip file")
		return False
	
	if not isdir(extract_dir):
		print("path: '" + extract_dir + "' isnt a directory, and cant extract the zip file into it")
		return False
		
	zf = ZipFile(zip_file_path, 'r')
	zf.extractall(extract_dir)
	zf.close()
	
	return True


""" build a path from mulitple strings

Args:
    zip_file_path (list) a list which contains all the 

Returns:
    string: the final string
"""
def build_path(path_components : list) -> str:
	if not isinstance(path_components, list):
		raise TypeError
	final_path = ""
	for comp in path_components:
		final_path = join(final_path, comp)
	return final_path
	
""" gets the path to the directory that contains the cudnn64_7.dll file

Args: 
	none

Returns:
	directory that contains the cudnn64_7.dll file
"""
def get_cudnn64_7_dir_path():
	while True:
		path = get_dir_path()
		if isfile(os.path.join(path, "cudnn64_7.dll")): return path
		print("this directory doesnt contain any cudnn64_7.dll path")

""" sets up the cudnn64_7 file settings up

Args:
	path_vars_file_name: the path to the settings file
	
Returns:
	nothing
"""
def save_path_vars(path_vars_file_name : str):
	print("write if cudnn64_7 exsits in your computer")
	cudnn64_7_exists = get_bool()
	
	if cudnn64_7_exists:
		print("enter cudnn64_7.dll directory path if it exsits")
		cudnn64_7_path = get_cudnn64_7_dir_path()
		
		path_vars_file = open(path_vars_file_name, 'w')
		path_vars_file.write(cudnn64_7_path)
		path_vars_file.close()


""" adds the cudnn64_7 to the system file path so this program could use the gpu

Args:
	path_vars_file_name (string): the path to the settings file
	
Returns:
	nothing

"""
def setup_path_vars(path_vars_file_name : str):
	if isfile(path_vars_file_name):
		path_vars_file = open(path_vars_file_name, "r")
		var_path = path_vars_file.read()
		path_vars_file.close()
		
		os.environ['PATH'] += ';' + var_path

""" count how many files there is in a directory
Args: directory path
Return: how many files in the directory
"""
def count_files_in_dir(dir_path):
	return len(listdir(dir_path))

""" counts how many images there are in the dataset

Args: 
	dataset_dir: the path to the dataset directory
	
Return:
	how many images there are in the dataset
"""
def count_imgs_in_dataset(dataset_dir : str):
	count = 0
	for dir in listdir(dataset_dir):
		count += count_files_in_dir(build_path([dataset_dir ,dir]))
	return int(count)

""" substracts lists
Args:
	subtrahend- the list that is the one that is substraced from
	minuend- list that is substracted from subtrahend
Return: 
	the difference between the lists (subtrahend-minuend)
"""
def list_substraction(subtrahend, minuend):
	difference = subtrahend.copy()
	for item in subtrahend:
		if item in minuend:
			difference.remove(item)
	return difference

""" load an image from the disk to memory
Args:
	the path to the image
	
Return:
	the image. the image is a 3dimensional numpy array
"""
def load_photo(img_path: str, img_width: int, img_height: int):
	image = Image.open(img_path)
	image = image.resize((img_width, img_height))
	image = image.convert("RGB")
	return image

""" print a prediciton from the model very nicely.
Args:
	img: the image to predict
	prediciton: a prediction from the single_prediction() function
	class_names: list thats hold the name of all the type of car logos
	
Returns:
	nothing
"""
def print_prediction(img, prediction, class_names):
	plt.grid(False)
	plt.xticks([])
	plt.yticks([])
	
	predicted_label = numpy.argmax(prediction)
	
	plt.imshow(img, cmap=plt.cm.binary)
	plt.xlabel("prediction: " + class_names[predicted_label])
	plt.show()
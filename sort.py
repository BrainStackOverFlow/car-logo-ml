from os import mkdir, listdir, path
from shutil import copy
from utils import list_substraction
folders = ["Alfa Romeo", "Audi", "BMW", "Chevrolet", "Citroen", "Dacia", "Daewoo",
	"Dodge", "Ferrari", "Fiat", "Ford", "Honda", "Hyundai", "Jaguar", "Jeep", 
	"Kia", "Lada", "Lancia", "Land Rover", "Lexus", "Maserati", "Mazda", 
	"Mercedes", "Mitsubishi", "Nissan", "Opel", "Peugeot", "Porsche", "Renault",
	"Rover", "Saab", "Seat", "Skoda", "Subaru", "Suzuki", "Tata", "Tesla",
	"Toyota", "Volkswagen", "Volvo"]

ignored_cars = []
final_cars = list_substraction(folders, ignored_cars)

class_names = final_cars

# create folders for the dataset
# this is needed so the train_geerator will be able to read correctly the images and to know their types
def make_folders(data_set_path):
	try:
		mkdir(data_set_path)
	except FileExistsError:
		pass
	
	try:
		mkdir(path.join(data_set_path, "train"))
	except FileExistsError:
		pass
	
	try:
		mkdir(path.join(data_set_path, "test"))
	except FileExistsError:
		pass

	try:
		mkdir(path.join(data_set_path, "all"))
	except FileExistsError:
		pass
	
	for fold in final_cars:
		try:
			mkdir(path.join(data_set_path, "train", fold))
		except FileExistsError:
			pass
			
	for fold in final_cars:
		try:
			mkdir(path.join(data_set_path, "test", fold))
		except FileExistsError:
			pass
	
	for fold in final_cars:
		try:
			mkdir(path.join(data_set_path, "all", fold))
		except FileExistsError:
			pass

# copy all files to thier designated folders
# this is needed so the train_geerator will be able to read correctly the images and to know their types
def copy_files(data_set_path: str, images_path: str):
	
	counter = {}
	
	for fold in final_cars:
		counter[fold] = 0
	
	for fil in listdir(images_path):
		for fold in final_cars:
			if fold in fil:
				counter[fold] = counter[fold] + 1
				copy(path.join(images_path, fil), path.join(data_set_path, "all", fold, fil))
				if (counter[fold] % 10 == 0):
					copy(path.join(images_path, fil), path.join(data_set_path, "test", fold, fil))
				else:
					copy(path.join(images_path, fil), path.join(data_set_path, "train", fold, fil))
				break


def sort_all_dirs(data_set_path: str, images_path: str):
	make_folders(data_set_path)
	copy_files(data_set_path, images_path)
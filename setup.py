import pip
import subprocess
import os
from os import system
from os.path import isfile
from subprocess import call
from utils import get_bool
from utils import get_file_path
from utils import get_dir_path
from utils import save_path_vars
from globalvars import path_vars_file_name	

# the packages the program needs to install
packages_to_install = ["keras", "tensorflow", "tensorflow-gpu", "pillow", "numpy", "pip", "matplotlib"]

""" installs the python packages needed to run main.py and updates pip
Args: 
	none
Returns:
	nothing
"""
def install_packages():
	
	print("write if you need to update or install all of the needed packages")
	should_install_packages = get_bool()
	
	if should_install_packages:
		call("pip install --upgrade pip", shell=True)
		call("pip install --upgrade " + ' '.join(packages_to_install), shell=True)

""" updates all of pip pacakges
Args: 
	none
Returns:
	nothing
"""
def update_packages():
	packages = eval(str(subprocess.run("pip list -o --format=json", shell=True, stdout=subprocess.PIPE).stdout, encoding='utf-8'))
	for pkg in packages:
		subprocess.run("pip install --upgrade " + pkg['name'], shell=True)

def main():
	print("setup script for machine learning project\n")

	print("beware, this script will update all of pip packages!")
	print("this script will modify the system path")
	print("do you wish to continue?")
	
	run_script = get_bool()
	
	if not run_script: return
	
	print("started script...")
	
	save_path_vars(path_vars_file_name)
	
	install_packages()
	
	print("finished script")
	
if __name__ == "__main__":
	main()
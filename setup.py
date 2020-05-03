import pip
import subprocess
import os
from os import system
from os.path import isfile
from subprocess import call
from Utils import get_bool
from Utils import get_file_path
from Utils import get_dir_path
from Utils import save_path_vars
	
packages_to_install = ["keras", "tensorflow-gpu", "pillow"]

def install_packages():
	call("pip3 install --upgrade " + ' '.join(packages_to_install), shell=True)

def update_packages():
	packages = eval(str(subprocess.run("pip3 list -o --format=json", shell=True, stdout=subprocess.PIPE).stdout, encoding='utf-8'))
	for pkg in packages:
		subprocess.run("pip3 install --upgrade " + pkg['name'], shell=True)

def main():
	print("setup script for machine learning project\n")

	print("beware, this script will update all of pip packages!")
	print("this script will modify the system path")
	print("do you wish to continue?")
	
	run_script = get_bool()
	
	if not run_script: return
	
	print("started script...")
	
	save_path_vars()
	
	update_packages()
	install_packages()
	
	print("finished script")
	
if __name__ == "__main__":
	main()
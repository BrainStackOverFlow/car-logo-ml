print("made by nadav baruch")
print("if anything crashes be sure to use the setup.py script first")

from ui import actions_strings, action_functions

from neuralnetworks import define_model
from utils import get_integer, setup_path_vars

import globalvars


def main():
	setup_path_vars(globalvars.path_vars_file_name)
	model = define_model()
	
	i = 0
	for string in actions_strings:
		i += 1
		print(str(i) + ". " + string)

	while True:
		print("what operation would you like to take?")
		
		operation = get_integer((1,len(actions_strings))) - 1
		
		if(operation == len(actions_strings) - 1): return
		else: action_functions[operation](model)

if __name__ == "__main__":
	main()
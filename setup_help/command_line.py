'''
	This folder contains all of the utilities to make the command line
	  interfaces work easer to work with! It transforms the list of
	  strings from the command line interface, to a dict 
'''
from dataclasses import dataclass

@dataclass
class Argument:
	name: str
	value: str
	priority: int
	used: bool

NAME_LIST = ['clean-cache', 'from-scratch', 'uninstall']

def process_args(sys_args):
	args = []
	for argument in sys_args:
		if argument[2:] == 'clean-cache':
			args.append(Argument('clean-cache', True, 0, False))
		elif argument[2:] == 'from-scratch':
			args.append(Argument('from-scratch', True, 0, False))
		elif argument[2:] == 'uninstall':
			args.append(Argument('uninstall', True, 0, False))

	arg_list = []
	for arg in args:
		arg_list.append(arg.name)

	for name in NAME_LIST:
		if name not in arg_list:
			args.append(Argument(name, False, -1, True))
	return args

def check_args(args):
	check = True
	for arg in args:
		if arg.name == 'clean-cache':
			if not ((arg.value == True) or (arg.value == False)):
				check = False

	return check

def does_cache_need_cleaning(args):
	need = False
	for arg in args:
		if arg.name == 'clean-cache' and arg.value == True and arg.used == False:
			arg.used = True
			need = True
			break
	return need

def ground_up_install(args):
	ground_up = False
	for arg in args:
		if arg.name == 'from-scratch' and arg.value == True and arg.used == False:
			ground_up = True
			arg.used = True
	return ground_up

def install_or_uninstall(args):
	install = True
	for arg in args:
		if arg.name == 'uninstall' and arg.value == True and arg.used == False:
			install = False
			arg.used = True
	return install
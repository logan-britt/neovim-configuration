'''
	This file moves the config and executable files into a position where
	  they will work on the system after they are either built or the
	  macros are replaced.
'''
from shutil import copytree, copy, rmtree
from sys import platform
from os import listdir, getcwd, chdir, getlogin, mkdir
from os.path import isdir, join

def deploy_python_plugins():
	pass

def move_lua_files_to_location():
	user_id = getlogin()

	if 'win' in platform:
		config_home = f'C:\\Users\\{user_id}\\AppData\\Local'
	else:
		config_home = f'home/{user_id}/.config'

	nvim_path = join(config_home, 'nvim')
	if not 'nvim' in listdir(config_home):
		mkdir(nvim_path)
	else:
		rmtree(nvim_path)
		mkdir(nvim_path)

	init_path = join(nvim_path, 'init.lua')
	copy('main/init.lua', init_path)
	for folder in listdir('main'):
		if isdir(folder):
			source_path = join('main', folder)
			destination_path = join(nvim_path, folder)
			copytree(source_path, destination_path)
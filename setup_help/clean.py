'''
	This file contains the basics needed to clean up the build and install
	  process so that we don't need to manuly deleate the detritus. It
	  also helps with the uninstall process.
'''
from os import getcwd, chdir, walk
from shutil import rmtree
from sys import platform
from getpass import getuser

def clean_cache():
	current_directory = getcwd()

	for (root, dirs, files) in walk( current_directory ):
		if '__pycache__' in dirs:
			rmtree(f'{root}/__pycache__')

	chdir( current_directory )

def clean_up_git_repos( neovim_path ):
	rmtree( neovim_path )

def uninstall_neovim():
	if 'win' in platform:
		path = 'C:\\Program Files\\Neovim'
		data_path = f'C:\\Users\\{getuser()}\\AppData\\Local\\nvim-data'
	else:
		path = f''
		data_path = ''
	rmtree(path)
	rmtree(data_path)
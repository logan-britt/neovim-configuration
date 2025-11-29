'''
	This file contains the basic utilities for pulling the nessery files
	  off of the internet and then build out and install the programs
	  that are related to them.
'''
from subprocess import run
from os import chdir, getcwd
from sys import platform
from shutil import copy

def download_source( neovim_path ):
	run(['git', 'clone', 'https://github.com/neovim/neovim.git', neovim_path])
	print()

def build_from_scratch( neovim_path ):
	current_dir = getcwd()
	chdir(neovim_path)
	
	if 'win' in platform:
		run(['cmake', '-S', 'cmake.deps', '-B', '.deps', '-G', 'Ninja', '-D', 'CMAKE_BUILD_TYPE=Release'])
		run(['cmake', '--build', '.deps', '--config', 'Release'])
		run(['cmake', '-B', 'build', '-G', 'Ninja', '-D', 'CMAKE_BUILD_TYPE=Release'])
		run(['cmake', '--build' 'build', '--config', 'Release'])
	else:
		pass
	
	chdir('build')
	run(['ninja', 'install'])

	chdir(current_dir)
	print()
from sys import argv

from setup_help.command_line import process_args, check_args, does_cache_need_cleaning
from setup_help.command_line import ground_up_install, install_or_uninstall
from setup_help.clean import clean_cache, clean_up_git_repos, uninstall_neovim
from setup_help.install import download_source, build_from_scratch
from setup_help.lua import install_lua
from setup_help.move_files import move_lua_files_to_location, deploy_python_plugins
from setup_help.rust import deploy_and_compile_rust_plugins
from setup_help.c_and_cxx import deploy_and_compile_c_and_cxx_plugings

TEMPORARY_NEOVIM_DIR = 'neovim-dir'
TEMPORARY_LUA_DIR = 'lua-dir'
TEMPORARY_POWERSHELL_DIR = 'powershell-dir'
TEMPORARY_NEOVIDE_DIR = 'neovide-dir'

def main(sys_args):
	args = process_args( sys_args )
	
	args_validated = check_args( args )
	if not args_validated:
		print('The arguments passed to the setup script were not valid!')
		print('\tYou need to validate the commands sent into the system.')
		print('\tPlease check the documentation, thank you!')
		exit()

	if install_or_uninstall( args ): # returns true if installing or false otherwise!
		if ground_up_install( args ):
			download_source( TEMPORARY_NEOVIM_DIR )
			install_lua( TEMPORARY_LUA_DIR )
			build_from_scratch( TEMPORARY_NEOVIM_DIR )
			clean_up_git_repos( TEMPORARY_NEOVIM_DIR )

		move_lua_files_to_location()
		deploy_python_plugins()

		deploy_and_compile_rust_plugins()
		deploy_and_compile_c_and_cxx_plugings()

	else:
		uninstall_neovim()

	if does_cache_need_cleaning( args ):
		clean_cache()

if __name__ == '__main__':
	main( argv[1:] )
-- This file contains the user created commands that are held
--   in lua. There also the commands created in python scripts
--   but they will be documented elsewhere. The functions
--   will be documented indeviduley below!

-- This is a test command to print a hello world
vim.api.nvim_create_user_command("Hello",
	function(opt)
		print('Hello Logan!')
	end,
	{
		nargs = 0,
	}
)

-- This command does something!
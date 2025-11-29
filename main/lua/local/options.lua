-- Here we set the basic editor settings like the line number settings
--   and the tab and space settings
vim.opt.relativenumber = true
vim.opt.number = true
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true
vim.opt.autoindent = true

-- Here we place the option settings for the quto read and write
--   settings. Autoread reads the file if it is changed outside
--   of neovim. Autowrite writes the file if it is changed in
--   neovim.
vim.opt.autowrite = false
vim.opt.autoread = true

-- Here we store the option settings for backup files and
--   folders. The way that backup dirs work is that neovim will search
--   through the list and pick the first one that can work. If
--   neovim finds non of the files work, it will try to create the
--   last one.
vim.opt.backupdir = {
	'D:\\Data\\NeovimBackups', 
	'C:\\Users\\Logan\\AppData\\NeovimBackups',
	'/data/NeovimBackups', 
	'/home/logan/NeovimBackups', 
	'LocalNeovimBackups'
}
vim.opt.backup = true

-- Here we place the option settings for command line window.
--   The code handels the setting of the shell interpreter. It
--   splits the algorithm between the windows half and the
--   unix half. We then set the size of the command line window.
local is_windows = package.config:sub(1, 1) == '\\' 
if is_windows then 
	local shell = vim.fn.system({'where.exe', ''})
	local nulls_to_cull = 1
	vim.opt.string = string.sub(shell, 1, string.len(shell) - nulls_to_cull)
	if vim.opt.shell == '' or vim.opt.shell = nil then
		shell = vim.fn.system({'which', 'powershell'})
    	vim.opt.shell = string.sub(shell, 1, string.len(shell) - nulls_to_cull)
	end
else 
	local shell = vim.fn.system({'which', 'zsh'})
	local nulls_to_cull = 1
	vim.opt.shell = string.sub(shell, 1, string.len(shell) - nulls_to_cull)
	if vim.opt.shell == "" or vim.opt.shell == nil then
    	shell = vim.fn.system({'which', 'bash'})
    	vim.opt.shell = string.sub(shell, 1, string.len(shell) - nulls_to_cull)
	end
end

vim.opt.cmdwindheight = 0
vim.opt.cmdheight = 0

-- Here we place the clipboard settings for the configuration
vim.opt.clipboard = 'unnamedplus'

-- Here we highlight the 81th colome so that I can keep formating consistant
vim.opt.colorcolumn = "81"

-- Here we have the option to ignore certain file and folder types
vim.opt.wildignore = {
	'*.o',
	'*.a',
	'*.dll',
	'*.lib',
	'__pycache__',
}

-- Here we set the spell checker to off, mabey turn it on later
vim.opt.spell = false

-- Here 
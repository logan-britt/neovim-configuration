-- This is the main file for the global setup for the basic neovim
--   configuration.
require('local.options')
require('local.commands')
require('local.autocmd')
require('local.keymaps')

-- These files for the setup of the language server and auto-colmpleat.
--   I might also fuck around with some spell checking...
--require('lsp.setup')
--require('lsp.autocmp')
--require('lsp.spell')
--require('lsp.chunck')
--require('lsp.')
--require('lsp.')
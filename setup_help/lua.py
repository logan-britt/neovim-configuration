import requests
from bs4 import BeautifulSoup

LUA_URL = 'https://www.lua.org/download.html'

'''
    This is the file soley dedicated to downloading and building a lua 
      interpreter from scratch so that the system works as intended.
      That is because the neovim program needs a lua interpreter to function.
'''
def download_lua( lua_dir ):
  lua_request_data = requests.get( LUA_URL )
  lua_data_structured = BeautifulSoup( lua_request_data.content, 'html.parser' )  

  menu = lua_data_structured.find( 'div', class_='menubar' )
  for tag in menu.find_all( 'a' ):
    if tag.:
      pass
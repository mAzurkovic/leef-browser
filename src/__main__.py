#!/usr/bin/python
#===================================#
# Author: Mattias A. Zurkovic       #
# ----------------------------------#
# This is the main.py file for      #
# the Leef browser.                 #
#===================================#

import sys
from Tkinter import *
import webkit, gtk

#===================================#

# session_url stores all the URLs the user has been to in this current session
session_url =[]

def __init__():
#  __window__(gtk.Window())
  print('Welcome to Leef. An open-source and light-weight browser for the modern web.')
  print('@browser-end')


# Go to the URL
def goto(widget):
  default_start_page = 'http://www.google.com'
  url_address = address_bar.get_text()
 
  if len(url_address) == 0:
    www.open(default_start_page)
  
  # auto add 'http://' to start of URL
  if url_address[0] != 'h':
    if url_address[1:6] != 'ttp://':
      if url_address.find('.com'):
        # Add 'http://'
        www.open('http://' + url_address)
        session_url.append('http://' + url_address)
        print(session_url)
      else:
        www.open('http://www.google.com/#q=' + url_address)
         
  else:
    www.open(url_address)
    session_url.append(url_address) 
    print(session_url)

# Search capabilites - if user does not enter proper URL, just enters a string, then search Google
def check_search(widget):
  # The string the user typed in ADDRESS BAR
  url_ans = address_bar.get_text()
  url_traits = ['http://', '.com', '.ca', '.net']  
  
  if url_ans.find(url_traits):
    goto(url_ans)
  else:
    www.open('http://google.com/#q=' + url_ans)


def new_window(widget):
  print('Window created!') 

  www = webkit.WebView()
  scroll_bar = gtk.ScrolledWindow()
  scroll_bar.add(www)

  window = gtk.Window()
  window.set_title("Leef Browser")
  window.connect('destroy', lambda w: gtk.main_quit())
  window.set_screen
  window.set_size_request(1368, 768)
  window.set_position(gtk.WIN_POS_CENTER)

  container = gtk.VBox()
  window.add(container)

  top_div = gtk.HBox()
  container.pack_start(top_div, False)

  address_bar = gtk.Entry()
  top_div.pack_start(address_bar)


  goto_button = gtk.Button('go!')
  goto_button.connect('clicked', goto)
  # Search button
  search_button = gtk.Button('Search')
  search_button.connect('clicked', check_search)
  # New window button
  new_window_button = gtk.Button('+')
  new_window_button.connect('clicked', new_window)

  top_div.pack_start(goto_button)
  top_div.pack_start(search_button)
  top_div.pack_start(new_window_button)

  container.pack_start(scroll_bar)

  window.show_all()
  gtk.main()

#-----------------------------------------

# Below the window is defined
www = webkit.WebView()
scroll_bar = gtk.ScrolledWindow()
scroll_bar.add(www)

window = gtk.Window()
window.set_title("Leef Browser")
window.connect('destroy', lambda w: gtk.main_quit())
window.set_screen
window.set_size_request(1368, 768)
window.set_position(gtk.WIN_POS_CENTER)

container = gtk.VBox()
window.add(container)

top_div = gtk.HBox()
container.pack_start(top_div, False)

# Back and forward buttons
back_button = gtk.Button("<")
for_button = gtk.Button(">")
top_div.pack_start(back_button)
top_div.pack_start(for_button)

# Address/URL bar
address_bar = gtk.Entry()
address_bar.set_text("Enter the website URL")
top_div.pack_start(address_bar)

goto_button = gtk.Button('go!')
goto_button.connect('clicked', goto)
# Search button
search_button = gtk.Button('Search')
search_button.connect('clicked', check_search)
# New window button
new_window_button = gtk.Button('+')
new_window_button.connect('clicked', new_window)

top_div.pack_start(goto_button)
top_div.pack_start(search_button)
top_div.pack_start(new_window_button)

container.pack_start(scroll_bar)

window.show_all()
gtk.main()




# Initialize main.py => run program
__init__()


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

def __init__():
#  __window__(gtk.Window())
  print "Testin'"


# Function for creating/initializing the GUI for the browser
def generate_win():
  print('Welcome to Leef. An open-source and light-weight browser for the modern web.')
  
  root = Tk()
  root.title('Leef Browser')
  root.minsize(1024, 748)
  
  # adress_ans is the variable/input that will be the URL that the user types in.
  address_ans = StringVar(None)
  address_bar = Entry(textvariable = address_ans, width = 50)
  address_bar.pack()

  # GO Button
  goto_button = Button(text="go!", command=goto)
  goto_button.pack()  

  # Top menubar/navigation bar 
  menubar = Menu(root)
  filemenu = Menu(menubar, tearoff = 0)
  filemenu.add_command(label = 'New Window')
  menubar.add_cascade(label = 'File', menu = filemenu)

  if len(address_bar.get()) > 0:
    root.bind('<Return>', goto()) 
  else:
    print "Waiting for a URL..."


  root.mainloop()


# Go to the URL
def goto(widget):
  default_start_page = 'http://www.google.com'
  url_address = address_bar.get_text()
 
  if len(url_address) == 0:
    www.open(default_start_page)
  
  http = 'http://' 
  # auto add 'http://' to start of URL
  if url_address[0] != 'h':
    if url_address[1:6] != 'ttp://':
      if url_address.find('.com'):
        # Add 'http://'
        www.open('http://' + url_address)
      else:
        www.open('http://www.google.com/#q=' + url_address)

  else:
    www.open(url_address)

 

# Search capabilites - if user does not enter proper URL, just enters a string, then search Google
def check_search(widget):
  # The string the user typed in ADDRESS BAR
  url_ans = address_bar.get_text()
  url_traits = ['http://', '.com', '.ca', '.net']  
  
  if url_ans.find(url_traits):
    goto(url_ans)
  else:
    www.open('http://google.com/#q=' + url_ans)



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

address_bar = gtk.Entry()
top_div.pack_start(address_bar)

goto_button = gtk.Button('go!')
goto_button.connect('clicked', goto)
top_div.pack_start(goto_button)

container.pack_start(scroll_bar)

window.show_all()
gtk.main()



def __window__(self):
  self.set_title("Leef Browser")
  self.set_size_request(1368, 768)
  self.set_position(gtk.WIN_POS_CENTER)
  self.connect("destroy", gtk.main_quit)

  www = webkit.WebView()
  scroll_bar = gtk.ScrolledWindow()
  scroll_bar.add(www)

  container = gtk.VBox()
  self.add(container) 

  top_div = gtk.HBox()
  container.pack_start(top_div, False)

  address_bar = gtk.Entry()
  top_div.pack_start(address_bar)

  goto_button = gtk.Button('go!')
  goto_button.connect('clicked', goto)

  #search_button = gtk.Button('Search')
  goto_button.connect('clicked', check_search) 
  
  #top_div.pack_start(search_button)
  top_div.pack_start(goto_button)

  container.pack_start(scroll_bar)

 # self.show_all()
 # getk.main()




# Initialize main.py => run program
__init__()

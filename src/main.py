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
  generate_win()

global address_bar

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
def goto():  
  url_address = address_bar.get_text()
  web.open(url_address)



# Initialize main.py => run program
__init__()

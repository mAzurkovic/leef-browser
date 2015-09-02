#===================================#
# Author: Mattias A. Zurkovic       #
# ----------------------------------#
# This is the main.py file for      #
# the Leef browser.                 #
#===================================#

import sys
from Tkinter import *

def __init__():
  generate_win()

# Function for creating/initializing the GUI for the browser
def generate_win():
  print('Welcome to Leef. An open-source and light-weight browser for the modern web.')
  
  root = Tk()
  root.title('Leef Browser')

  root.mainloop()

# Initialize main.py => run program
__init__()

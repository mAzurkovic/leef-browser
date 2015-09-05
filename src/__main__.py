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

class LeefMain(gtk.Window):

  def __init__(self):
    gtk.Window.__init__(self)
    self.set_border_width(10)
    self.set_size_request(1368, 768)    

    session_url =[]    

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
  
      www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + url_ans)

    # Function for going to prev. page
    def goto_back(widget):
      print "Leef Browser: @BACK"

    def new_window(widget):
      window = LeefMain()
      window.connect("delete-event", gtk.main_quit)
      window.show_all()
      gtk.main()


    search_engine_names = ["Google", "Duck Duck Go", "Yahoo", "Bing"]

    # Below the window is defined
    www = webkit.WebView()
    scroll_bar = gtk.ScrolledWindow()
    scroll_bar.add(www)

    container = gtk.VBox()
    self.add(container)

    top_div = gtk.HBox()
    container.pack_start(top_div, False)

    # Back and forward buttons
    back_button = gtk.Button("<")
    back_button.connect("clicked", goto_back)
    for_button = gtk.Button(">")
    top_div.pack_start(back_button)
    top_div.pack_start(for_button)

    # Address/URL bar
    address_bar = gtk.Entry()
    address_bar.set_text("Enter the website URL")
    top_div.pack_start(address_bar)

    goto_button = gtk.Button('go!')
    goto_button.connect('clicked', goto)
    top_div.pack_start(goto_button)

# Search bar
#search_bar = gtk.Entry()
#search_bar.set_text(search_engine_names[0] + " Search")
#top_div.pack_start(search_bar)

    # Search button
    search_button = gtk.Button('Search')
    search_button.connect('clicked', check_search)
    # New window button
    new_window_button = gtk.Button('+')
    new_window_button.connect('clicked', new_window)

    top_div.pack_start(search_button)
    top_div.pack_start(new_window_button)

    container.pack_start(scroll_bar)
  


window = LeefMain()
window.connect("delete-event", gtk.main_quit)
window.show_all()
gtk.main()

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
    self.set_border_width(5)
    self.set_size_request(1368, 768)    
    
    # This array stores the URLs/Websites the user has gone in the currect Browser session
    session_url =[]    
    # Stores all the bookmarks the users has
    bookmarks = []

    # Go to the URL
    def goto(widget):
      default_start_page = 'http://www.google.com'
      url_address = address_bar.get_text()
 
      # auto add 'http://' to start of URL
      if url_address[0] != 'h':
        if url_address[1:6] != 'ttp://':
          # Add 'http://'
          www.open('http://' + url_address)
          session_url.append('http://' + url_address)
          print(session_url)
      
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
  
      www.open(session_url[0])
      

      
    def bookmark_page(widget):
      print("Leef Browser: @BOOKMARK")
      bookmarked_url = address_bar.get_text()
      print("Successfully bookmarked " + bookmarked_url)
      bookmarks.append(bookmarked_url)
      print(bookmarks)
      

    def new_window(widget):
      window = LeefMain()
      window.set_title("Leef Browser")
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
    back_button.set_tooltip_text("Previous page")
    back_button.set_size_request(width = 40, height = 30)
    back_button.connect("clicked", goto_back)
    top_div.pack_start(back_button, expand  = False)

    '''
    recent_address_store = gtk.ListStore(str)
    for url in session_url:
      recent_address_stroe.append([url])

    #address_bar = gtk.combo_box_entry_new_text()
  
    '''

    # Address Bar
    address_bar = gtk.Entry()
    address_bar.connect('activate', goto)
    address_bar.set_tooltip_text("Enter the website URL")
    top_div.pack_start(address_bar)

    # Goto Button
    goto_button = gtk.Button('Go!')
    goto_button.set_tooltip_text("Go to site")
    goto_button.connect('clicked', goto)
    top_div.pack_start(goto_button, expand = False, fill = False)

    # Search Bar
    search_bar = gtk.Entry()
    search_bar.connect("activate", check_search)
    search_bar.set_tooltip_text("Search the net")
    search_bar.set_size_request(width = 240, height = 33)
    top_div.pack_start(search_bar, expand = False, fill = False)

    # Search button
    search_button = gtk.Button('Search')
    search_button.set_tooltip_text("Google search")
    search_button.connect('clicked', check_search)
    top_div.pack_start(search_button, expand = False, fill = False)  
 
    # Divider
    divider = gtk.Label()
    divider.set_text(" | ")
    top_div.pack_start(divider, expand = False, fill = False)
 
    # Bookmark
    fav_button = gtk.Button("Bookmark")
    fav_button.set_tooltip_text("Bookmark page")
    fav_button.connect('clicked', bookmark_page)

    # New window button
    new_window_button = gtk.Button('+')
    new_window_button.set_tooltip_text("New Leef window")
    new_window_button.set_size_request(width = 40, height = 30)
    new_window_button.connect('clicked', new_window)

    top_div.pack_start(fav_button, expand = False, fill = False)
    top_div.pack_start(new_window_button, fill = False, expand = False)

    container.pack_start(scroll_bar)
  

window = LeefMain()
window.set_title("Browser")
window.connect("delete-event", gtk.main_quit)
window.show_all()
gtk.main()

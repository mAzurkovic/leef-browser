#!/usr/bin/python
#===================================#
# Author: Mattias A. Zurkovic       #
# ----------------------------------#
# This is the __main.py__ file for  #
# the Leef browser.                 #
#===================================#

import sys
from Tkinter import *
import webkit, gtk

#===================================#

class LeefMain(gtk.Window):

  def __init__(self):
    gtk.Window.__init__(self)
   # self.set_border_width(5)
    self.set_default_size(1368, 768)    
    
    # This array stores the URLs/Websites the user has gone in the currect Browser session
    session_url =[]    
    # Stores all the bookmarks the users has
    bookmarks = []


    def goto_to(widget):
      text = address_bar.get_text()
      if text.startswith("http://"):
        www.open(text)
       # session_url.append(text)
       # print(session_url)

      elif text.endswith(".com"):
        www.open("http://" + text)
       # session_url.append("http://" + text)
       # print(session_url)

      # Use Duck Duck GO Search
      elif text.startswith("Duck Duck Go:"):
        ddg_from = text.find(":")
        ddg_search = text[ddg_from:-1]
        www.open("https://duckduckgo.com/?q=" + ddg_search)  
      # Use Bing - I know Bing lol
      elif text.startswith("Bing:"):
        bing_pos = text.find(":")
        bing_search = text[bing_pos:-1]
        www.open("https://www.bing.com/search?q=" + bing_search)
      # Yahoo Quick Search
      elif text.startswith("Yahoo:"):
        yahoo_pos = text.find(":")
        yahoo_search = text[yahoo_pos:-1]
        www.open("https://search.yahoo.com/search;_ylt=AwrTHQhZ_gFWLnEAqNBXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3NmcARncHJpZAM1Ljd6azNZVlJMLk5BbGd5cGR5OTJBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM0BHF1ZXJ5A3hheGEEdF9zdG1wAzE0NDI5NzEyMzM-?p=" + yahoo_search)  
      elif text.startswith("Google:"):
        google_pos = text.find(":")
        google_search = text[google_pos:-1]
        www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + google_search)
      # Default search is GOOGLE
      else:
        www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + text)
        #www.open("https://duckduckgo.com/?q=" + text)

#TODO: REMOVE Reg goto
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
      # URL in Address Bar
      typed_ans = address_bar.get_text()
      www.open(session_url[-2])
      #session_url.pop()
      del session_url[-2:]

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

 
    # Change title of browser - In top bar, states name of current site and index of that site 
    def title(view, frame, title):
      self.set_title(title)

    # Changes the URI in the address bar to display the current site url the user is on
    def link_check(view, frame):
      new_uri = frame.get_uri()
      session_url.append(new_uri)
      address_bar.set_text(new_uri) 
      print(session_url)

    search_engine_names = ["Google", "Duck Duck Go", "Yahoo", "Bing"]
    search_engine_home = ["http://www.google.com", "http://www.duckduckgo.com"]

    # Below the window is defined
    www = webkit.WebView()
    scroll_bar = gtk.ScrolledWindow()
    scroll_bar.add(www)

    # Default browser piage - (When browser is launched it diplays this)
    www.open("http://www.google.com")

    # Set event for title change
    www.connect("title-changed", title)
    # Event for link in addressbar to change
    www.connect("load-committed", link_check)

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

    # Address Bar
    address_bar = gtk.Entry()
    address_bar.connect('activate', goto_to)
    address_bar.set_tooltip_text("Enter the website URL")
    top_div.pack_start(address_bar)

    # Goto Button
    goto_button = gtk.Button('Go!')
    goto_button.set_tooltip_text("Go to site")
    goto_button.connect('clicked', goto)
    #top_div.pack_start(goto_button, expand = False, fill = False)

    # Search Bar
    search_bar = gtk.Entry()
    search_bar.connect("activate", check_search)
    search_bar.set_tooltip_text("Search the net")
    search_bar.set_size_request(width = 240, height = 33)
    search_bar.set_text("Search")
   # top_div.pack_start(search_bar, expand = False, fill = False)

    # Search button
    search_button = gtk.Button('Search')
    search_button.set_tooltip_text("Google search")
    search_button.connect('clicked', check_search)
    #top_div.pack_start(search_button, expand = False, fill = False)  
 
    # Divider
    divider = gtk.Label()
    divider.set_text(" | ")
    #top_div.pack_start(divider, expand = False, fill = False)
 
    # Bookmark
    fav_button = gtk.Button("Bookmark")
    fav_button.set_tooltip_text("Bookmark page")
    fav_button.connect('clicked', bookmark_page)

    # New window button
    new_window_button = gtk.Button('+')
    new_window_button.set_tooltip_text("New Leef window")
    new_window_button.set_size_request(width = 40, height = 30)
    new_window_button.connect('clicked', new_window)

    # top_div.pack_start(fav_button, expand = False, fill = False)
    top_div.pack_start(new_window_button, fill = False, expand = False)

    container.pack_start(scroll_bar)
  

window = LeefMain()
window.set_title("Leef Browser")
window.connect("delete-event", gtk.main_quit)
window.show_all()
gtk.main()

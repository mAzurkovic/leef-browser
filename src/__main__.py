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
import ConfigParser
from ConfigParser import SafeConfigParser

#===================================#

class LeefMain(gtk.Window):

  def __init__(self):
    gtk.Window.__init__(self)
    self.set_default_size(1368, 768)    
    self.set_border_width(2)  
  
    # This array stores the URLs/Websites the user has gone in the currect Browser session
    session_url =[]    
    # Stores all the bookmarks the users has
    bookmarks = []
    #
    default_engine = "Google"

    # CONFIGs
    config = ConfigParser.ConfigParser()

    # Open a WRITABLE config.ini file
    file = open("config.ini", "w")
    parser = SafeConfigParser()

    config.add_section("DEFAULT_ENGINE")
    config.set("DEFAULT_ENGINE", "Engine Name", "Google")
    with open("config.ini", "wb") as config_file:
        config.write(config_file)


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
      
      # Check config.ini file and see what user set as default SEARCH ENGINE
      else:
        
        name = config.get("DEFAULT_ENGINE", "Engine Name")
  
        try:     
          if name == "Duck Duck Go":
            www.open("https://duckduckgo.com/?q=" + text)
          elif name == "Bing":
            www.open("https://www.bing.com/search?q=" + text)
          elif name == "Google":
            www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + text)
          else:
            www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + text)
        except NoSectionError:
	  config.add_section("DEFAULT_ENGINE")
          config.set("DEFAULT_ENGINE", "Engine Name", "Google")
      #new_engine = config.get("DEFAULT_ENGINE", "Engine Name")
      #print new_engine
      # write changes back to the config file
          with open("config.ini", "wb") as config_file:
      	    config.write(config_file)

          www.open("https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=" + text)


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
    engine_url = ["https://www.google.ca/?gfe_rd=cr&ei=5NnpVfajF4qV8QfglLCQBg&gws_rd=ssl#q=", "https://duckduckgo.com/?q="]  
 
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
    back_icon = gtk.Image()
    back_icon.set_from_stock(gtk.STOCK_GO_BACK, gtk.ICON_SIZE_BUTTON)
    back_button = gtk.Button()
    back_button.add(back_icon)
    back_button.set_tooltip_text("Previous page")
    back_button.set_size_request(width = 40, height = 30)
    back_button.connect("clicked", goto_back)
    top_div.pack_start(back_button, expand  = False)

    # Refresh button
    refresh_icon = gtk.Image()
    refresh_icon.set_from_stock(gtk.STOCK_REFRESH, gtk.ICON_SIZE_BUTTON)
    refresh_button = gtk.Button()
    refresh_button.add(refresh_icon)
    refresh_button.connect("clicked", goto_to)
    refresh_button.set_size_request(width = 40, height = 30)
    top_div.pack_start(refresh_button, fill = False, expand = False)


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
    fav_icon = gtk.Image()
    fav_icon.set_from_stock(gtk.STOCK_APPLY, gtk.ICON_SIZE_BUTTON)
    fav_button = gtk.Button()
    fav_button.add(fav_icon)
    fav_button.set_tooltip_text("Bookmark page")
    fav_button.set_size_request(width = 40, height = 30)
    fav_button.connect('clicked', bookmark_page)
    top_div.pack_start(fav_button, fill = False, expand = False)

    # New window button
    new_icon = gtk.Image()
    new_icon.set_from_stock(gtk.STOCK_ADD, gtk.ICON_SIZE_BUTTON) 
    new_window_button = gtk.Button()
    # Implement the image object to the button
    new_window_button.add(new_icon)
    new_window_button.set_tooltip_text("New Leef window")
    new_window_button.set_size_request(width = 40, height = 30)
    new_window_button.connect('clicked', new_window)
    top_div.pack_start(new_window_button, fill = False, expand = False)


    # Change default engine to GOOGLE
    def change_to_google(widget):
      print("Leef Browser: @ CHANGE DEFAULT ENGINE TO GOOGLE")
      config.add_section("DEFAULT_ENGINE")
      config.set("DEFAULT_ENGINE", "Engine Name", "Google")
      #new_engine = config.get("DEFAULT_ENGINE", "Engine Name")
      #print new_engine
      # write changes back to the config file
      with open("config.ini", "wb") as config_file:
        config.write(config_file)


    # Change default engine to DUCK DUCK GO 
    def change_to_ddg(widget):
      print("Leef Browser: @CHANGE DEFAULT ENGINE TO DDG")
      config.remove_section("DEFAULT_ENGINE")
      config.add_section("DEFAULT_ENGINE")
      config.set("DEFAULT_ENGINE", "Engine Name", "Duck Duck Go")
      with open("config.ini", "wb") as config_file:
        config.write(config_file)



 
    # Change default engine to BING  
    def change_to_bing(widget):
      print("Leef Browser: @CHANGE DEFAULT ENGINE TO BING")
      
      config.add_section("DEFAULT_ENGINE")
      config.set("DEFAULT_ENGINE", "Engine Name", "Bing")
      #new_engine = config.get("DEFAULT_ENGINE", "Engine Name")
      #print new_engine
      # write changes back to the config file
      with open("config.ini", "wb") as config_file:
        config.write(config_file)
 
    def settings_window(widget):
      print("Leef Browser: @SETTINGS WINDOW")
      settings_win = gtk.Window()
      settings_win.set_title("Settings")
      settings_win.connect("delete-event", gtk.main_quit)
      settings_win.set_border_width(10)

      vbox = gtk.VBox(spacing=6)

      engine_hbox = gtk.HBox()
    
      settings_win.add(vbox) 
      vbox.pack_start(engine_hbox, False)

      pick_engine = gtk.Label("Choose default search engine: ")
      engine_hbox.pack_start(pick_engine)
     
      google_button = gtk.Button("Google")
      google_button.connect("clicked", change_to_google)
      engine_hbox.pack_start(google_button, fill = False, expand = False) 

      ddg_button = gtk.Button("Duck Duck Go")
      ddg_button.connect("clicked", change_to_ddg)
      engine_hbox.pack_start(ddg_button, fill = False, expand = False)

      bing_button = gtk.Button("Bing")
      bing_button.connect("clicked", change_to_bing)
      engine_hbox.pack_start(bing_button, fill = False, expand = False)


      settings_win.show_all()
      gtk.main()
      


    # Settings button
    settings_icon = gtk.Image()
    settings_icon.set_from_stock(gtk.STOCK_PREFERENCES, gtk.ICON_SIZE_BUTTON)
    settings_button = gtk.Button()
    settings_button.add(settings_icon)
    settings_button.connect("clicked", settings_window)
    settings_button.set_size_request(width = 40, height = 30)
    top_div.pack_start(settings_button, fill = False, expand = False)

    # About button
    about_icon = gtk.Image()
    about_icon.set_from_stock(gtk.STOCK_INFO, gtk.ICON_SIZE_BUTTON)
    about_button = gtk.Button()
    about_button.add(about_icon)
    about_button.set_tooltip_text("About Leef")
    about_button.set_size_request(width = 40, height = 30)
    #about_button.connect("clicked", goto_back)
    top_div.pack_start(about_button, expand  = False)


    # Include scroll BAR
    container.pack_start(scroll_bar)

  

window = LeefMain()
window.set_title("Leef Browser")
window.connect("delete-event", gtk.main_quit)
window.show_all()
gtk.main()


import os
import curses
import cursesmenu
from time import sleep
import subprocess
os.system('clear')
print("Loading System...")
sleep(1)
print("...")
sleep(2)
os.system('clear')
menu = cursesmenu.CursesMenu.make_selection_menu(["ChannelViewer", "Exit"], "Select an app")
menu.show()
menu.join()
selection = menu.selected_option
if selection == 0:
    os.system('clear')
    print("Loading...")
    sleep(2)
    os.system('clear')
    
    sleep(5)
if selection == 1:
    os.system('clear')
    print("")
    sleep(2)
    os.system('clear')
    print("Exiting Now")
    sleep(2)

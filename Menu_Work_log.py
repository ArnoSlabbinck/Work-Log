import datetime
import sys
import os
import errno

from time import gmtime, strftime
from time import sleep

import Delete_Save_Edit_Entries 
import add_new_work_log
import Previous_work_log

# For the user to enter he should solve a problem

def clear_screen():
    """Clear the screen"""
    try:
      os.system('cls')
    except:
      os.system('clear')


def start_app():
    """Starts the app"""
    clear_screen()
    welcome_user(ask_for_name())
    name_app()
    show_time()
    clear_screen()
    show_menu()


def show_home_menu():
    """Displays the main menu for the app."""
    clear_screen()
    show_menu()

def ask_for_name(): 
    """Ask for user name"""
    name = input("Enter fullname please:\n> ")
    clear_screen()
    return name

def show_time(): 
    print("Current time: \n")
    day_time = strftime("%a, %d %b %Y %H:%M:%S ", gmtime())
    print(day_time)
    sleep(3)

def welcome_user(name):
    """welcome the user"""
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("Good morning {}, and welcome to the work log.\n".format(name))
    elif 12 <= current_time.hour < 18:
        print("Good afternoon {}, and welcome to the work log .\n".format(name))
    else:
        print("Good evening {}, and welcome to your work log.\n".format(name))
    
    sleep(4)

def name_app(): 
    clear_screen()
    print("WORK SMARTER!!")

def show_menu():
    """A menu that shows if the user wants  to add a new entry or lookup previous entries."""
    while True:
        print("Menu ")
        print("""
    [A]dd a new entry 
    [L]ookup previous entries
    [Q]uit")
        """)
        menu_option = input("\n What would you like to do ?\n> ").strip()

        if menu_option.upper() in "ALQ":
            if menu_option.upper() == 'A':
                add_new_work_log.add_log()
                break
                
            elif menu_option.upper() == 'L':
                Previous_work_log.show_previous_entries_menu()
                break
                 
            elif menu_option.upper() == 'Q':
                input("\n Thank you, until next time. Press enter to leave. ")
                clear_screen()
                sys.exit
                break
        else:
            input("\n Invalid option. Please use the menu correctly. Answer with A, Q or L. Press enter to continue... ")
            show_menu()
            break



if __name__ == "__main__":
    start_app()
    
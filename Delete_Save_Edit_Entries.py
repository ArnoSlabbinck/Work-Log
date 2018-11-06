import csv
import datetime

import Confirm_work_log
import add_new_work_log
import Menu_Work_log

from time import sleep



def delete_entry(task, time_spent, date, comments):

    while True:
        delete_it = input("\n Are you sure you want to delete, [Y]es or [N]o? ")
        if not delete_it:
            input("\n Please confirm whether to delete or not. Press enter to continue... ")
            continue

        elif delete_it.upper() in "YN":
            if delete_it.upper() == 'Y':
                task, time_spent, date, comments = (None,)*4
                Menu_Work_log.show_menu()
                break

            elif delete_it.upper() == 'N':
                Menu_Work_log.clear_screen()
                Confirm_work_log.show_all_entries(task, time_spent, date, comments)
                break
        else:
            input("\n Invalid input. Please use either 'Y' or 'N'. Press enter to continue... ")


def save_entry(task, time_spent, date, comments): 
    """Saves the user's entries """
    Menu_Work_log.clear_screen() 

    with open('work_log.csv', 'a', newline='') as csvfile: # Make a CSV file folder 
        entry_fieldnames = ['Task name', 'Time spent', 'Date', 'Comments']
        filewriter = csv.DictWriter(csvfile, fieldnames=entry_fieldnames)
        filewriter.writerow({
            'Task name': task,
            'Time spent': time_spent,
            'Date': date,
            'Comments': comments})
            
    input(" Entry saved! Press enter to continue...")
    Menu_Work_log.clear_screen()
    Menu_Work_log.show_menu()
       

def edit_entry(task, time_spent, date, comments):
    """Allows the user to edit their entry"""
    Menu_Work_log.clear_screen()
    print(" "*6 + " Edit Entry " + " "*6)

    change_entry = [task, time_spent, date, comments]
    entry_keys = iter(['Task name', 'Time Spent', 'Date', 'Comments'])
    entry_items = iter([task, time_spent, date, comments])

    index = 0

    for _ in range(len(change_entry)):
        while True: 
            pf = next(entry_keys)
            print("Current {} : {}\n".format(pf, next(entry_items)))
            answer = input("Do you want to edit {}. [Y]ess or [N]o\n> ". format(pf))
            if answer == "Y": 
                for i in change_entry: 
                    i = input("Change into:\n> ")

                    if index == 0: 
                        task = i

                    elif index == 1:
                        time_spent = i

                    elif index == 2: 
                        date = i

                    elif index == 3:
                        comments = i
                    break
                    
                break

            elif answer == "N":
                break
            else: 
                input("Must answer with [Y]ess or [N]o. Try again.\n ")
                continue
        index += 1


    Confirm_work_log.show_all_entries(task, time_spent, date, comments)



    

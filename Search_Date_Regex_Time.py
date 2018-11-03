import Previous_work_log
import Menu_Work_log
import display_work_log
import add_new_work_log
import re
import datetime


from time import sleep


class Date:
    def date_options(self):
        while True:
            Menu_Work_log.clear_screen()
            current_entries = Previous_work_log.get_all_entries() # get all 
            option = input("Great! You have two options. You can choose between search through [E]xact date or [R]ange of date \n> ")
            
            if option == "E": 
                Date.search_exact_date(current_entries)
                break

            elif option == "R": 
                Date.search_by_date_range()
                break

            else:          
                input("This is an invalid input. Press enter to continue...")
                continue

                
    
    def search_exact_date(current_entries):
        Menu_Work_log.clear_screen() # Clear screen 
        entries_dates = Date.get_entry_dates(current_entries) # Get all dates from CSV file
        Date.print_entry_dates(entries_dates) # Show user all the dates he has in work log
        searched_entries = []

        while True:

            search_date = input("\n Enter a date (dd-mm-yyyy)\n>  ").strip() 

            if not search_date:
                input("\n Enter a date. Press enter to continue... ")
                continue

            if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}$', search_date):
                input("\n Invalid date. Date must be in the right format. Press enter to continue... ")
                continue

            if search_date not in entries_dates:
                input("\n Enter valid date. Pick a date from the above. Press enter to continue... ")
                continue

            else:
                for entry in current_entries:
                    if entry['Date'] == search_date:
                        searched_entries.append(entry)

                display_work_log.show_results(searched_entries)
                break

    
    def get_entry_dates(current_entries):
        search_date = []

        for entry in current_entries:
            if entry['Date'] not in search_date:
                search_date.append(entry['Date'])

        dates = sorted(search_date)
        return dates 


    def print_entry_dates(dates):
        """Prints dates passed to it."""
        print(" "*6 + " Dates " + ""*6)
        for date in dates:
            print("\n" + date)
    
    def search_by_date_range():
        """Makes a search based on a given date range"""
        Menu_Work_log.clear_screen()
        entries = Previous_work_log.get_all_entries()
        entry_dates = Date.get_entry_dates(entries)
        searched_entries = []
        search_dates = []

        while True:
            Menu_Work_log.clear_screen()
            Date.print_entry_dates(entry_dates)
            print("\n\n " + " "*3 + "-"*3 + " return with 'R' " + " "*3)
            range_date = input("\n Choose the date range like this (dd-mm-yyyy to dd-mm-yyyy): ")

            if not range_date:
                input("\n Kindly enter a date range. Press enter to continue... ")
                continue

            if range_date.upper() == "R":
                Previous_work_log.show_previous_entries_menu()
                break

            if not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}\s?to\s?[0-9]{2}-[0-9]{2}-[0-9]{4}$', range_date):
                input("\n Invalid date range. Press enter to continue... ")
                continue

            else:
     
                range_date = [date.strip() for date in range_date.split("to")]
                if range_date[0] not in entry_dates or range_date[-1] not in entry_dates:
                    input("\n Sorry, that's not good.Check the dates you've been given again. Be sure to enter in the correct format. Press enter to continue... ")
                    continue

                for entry_date in entry_dates:
                    if (entry_date >= range_date[0]) and (entry_date <= range_date[-1]):
                        search_dates.append(entry_date)

                for entry in entries:
                    if entry['Date'] in search_dates:
                        searched_entries.append(entry)

                display_work_log.show_results(searched_entries)

                break



def search_time():
    """Search by a specific time"""
    Menu_Work_log.clear_screen()
    entries = Previous_work_log.get_all_entries()
    new_Time_Spent = list()
    searched_entries = list()

    for entry in entries:
        Time_Spent = entry['Time Spent']
        Time_Spent = int(Time_Spent)
        Time_Spent = datetime.timedelta(minutes = Time_Spent)
        Time_Spent = str(Time_Spent)
        Time_Spent = Time_Spent[:-3]
        if Time_Spent not in new_Time_Spent:
            new_Time_Spent.append(Time_Spent)

    while True:
        Menu_Work_log.clear_screen()
        print("\n " + " Current Times ")
        for i in new_Time_Spent:
            print(" " + i + " ")
            sleep(1)

        search_time = add_new_work_log.ask_time_spent()
        search_time = str(search_time)
        for entry in entries:
            if (entry["Time Spent"] == search_time):
                searched_entries.append(entry)
        if not searched_entries:
            input("\n Sorry, no task available. Press enter to continue... ")
            continue
        else:
            display_work_log.show_results(searched_entries)
            break


def search_text(): 
    """Searches the entries by any string or regular expression from the user."""
    entries = Previous_work_log.get_all_entries()
    while True:
        Menu_Work_log.clear_screen()
        print( " Search by Text or Regular expression " )
        print("\n\n "+ " Go back with [R]eturn")
        searched_entries = []
        search_input = input("\n\n Enter your text expression: ")

        if not search_input:
            input("\n You didn't enter anything. Press enter and try again. ")
            continue

        if search_input.upper() == "R":
            Previous_work_log.show_previous_entries_menu()
            break

        else:
            search_token = r'' + search_input
            for entry in entries:
                if (re.search(search_token, entry['Task name']) or
                    re.search(search_token, entry['Comments'])):
                    if entry not in searched_entries:
                        searched_entries.append(entry)
                        
            # print(searched_entries)
            if not searched_entries:
                input("\n Sorry, no results by your search. Press enter and try again... ")
                continue
            else:
                display_work_log.show_results(searched_entries)
            break



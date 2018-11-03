import Menu_Work_log
import Search_Date_Regex_Time
import csv

def show_previous_entries_menu():
    """Presents to the user list of options to search for previous entries."""
    date = Search_Date_Regex_Time.Date()

    while True:
        Menu_Work_log.clear_screen()
        print(" "*6 + " Lookup Previous Entries " + " "*6)
        print("""
        Search by [D]ate
        Search by [T]ime spent
        Search by [R]egex or Text
        Go back - [H]ome menu
        """)
        menu_option = input("\n How would you like to search?\n> ").strip()


        if menu_option.upper() in "DTRH":
         
            if menu_option.upper() == "D": 
                date.date_options()
                break

            elif menu_option.upper() == "T":
                Search_Date_Regex_Time.search_time()
                break

            elif menu_option.upper() == "R": 
                Search_Date_Regex_Time.search_text()
                break

            elif menu_option.upper() == "H":
                Menu_Work_log.clear_screen()
                Menu_Work_log.show_menu()
                break 

        else:
            input("\n Invalid input. Choose from the menu. Press enter to continue... ")
            continue


def get_all_entries():
    """Reads all the logged entries."""
    with open('work_log.csv', 'r') as csvfile:
        entry_fieldnames = ['Task name', 'Time Spent', 'Date', 'Comments']
        file_reader = csv.DictReader(csvfile, fieldnames=entry_fieldnames)
        entries = list(file_reader)
        return entries

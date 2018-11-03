import add_new_work_log
import Menu_Work_log
import Delete_Save_Edit_Entries
import display_work_log

def show_all_entries(task, time_spent, date, comments):
    change_entry = [task, time_spent, date, comments]
    names = ['Task name', 'Time Spent', 'Date', 'Comments'] 
    while True:
        Menu_Work_log.clear_screen()
        print(" Pay close attention if all entries are correct. The following entries are: \n")
        display_work_log.print_all_entries(change_entry, names)
        print(" If want to change something that's still possible")
        confirm_task_entry(task, time_spent, date, comments)
        break

def confirm_task_entry(task, time_spent, date, comments):
    """Ask user whether to save or edit entries"""

    while True:
        response = input("Do you want to [S]ave or [E]dit or [D]elete entries?\n> ").upper()

        possible_responses = ["S", "D", "E"]

        if response in possible_responses: 
            if response == "S":
                Delete_Save_Edit_Entries.save_entry(task, time_spent, date, comments)
                break
            elif response == "D" : 
                Delete_Save_Edit_Entries.delete_entry(task, time_spent, date, comments)
                break
            else: 
                Delete_Save_Edit_Entries.edit_entry(task, time_spent, date, comments)
                break
        else: 
            input("That's an invalid input. Please only enter [S]ave or [E]dit or [D]elete entries. Press enter to continue...")
            continue



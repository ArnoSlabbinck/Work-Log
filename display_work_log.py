import Search_Date_Regex_Time
import Menu_Work_log
import Previous_work_log
import Delete_Save_Edit_Entries

from time import sleep


def print_all_entries(searched_entries, entry_names):
    # Gives the user the task, time spent, date and comments he gave in 
    for name, entry in zip(entry_names, searched_entries):
        print("{}: {}\n".format(name, entry)) 


def show_results(searched_entries):
    count = 0

    while True:
        Menu_Work_log.clear_screen()
        entry_names = iter(["Task name", "Time Spent", "Date", "Comments"]) 
        enter_choses = ["[N]ext", "[P]revious", "[E]dit", "[D]elete", "[R]eturn"]
        print("\n " + " "*3 + " Search Results " + " "*3) 
        searched_item = searched_entries[count]
        entries = list()
        for i in range(4):
                entry = next(entry_names)
                print("{} : {}".format(entry, searched_item[entry]))
                entries.append(searched_item[entry])
        
        print("Result {} of  {}\n".format(count+1, len(searched_entries)))
        if count == 0:
               enter_choses.remove('[P]revious')
        # Disable the [N]ext option at the last instance of the results..
        try:
                if count == len(searched_entries) - 1:
                        entry.remove('[N]ext')
        except AttributeError: 
                count -= 1
        

        page_options = ', '.join(enter_choses) + ': '

        navigate = input("\n {} to search menu \n> ".format(page_options)).strip()

        if navigate.upper() in "NPR" and navigate.upper() in page_options:

                if navigate.upper() == "P":
                        count -= 1
                        continue
                elif navigate.upper() == "N":
                        count += 1
                        continue
                elif navigate.upper() == "R":
                        break

                elif navigate.upper() == "E":
                        Delete_Save_Edit_Entries.edit_entry(entries[0], entries[1], entries[2], entries[3])
                        break

                elif navigate.upper() == "D": 
                        Delete_Save_Edit_Entries.delete_entry(entries[0], entries[1], entries[2], entries[3])
                        break
                else:
                    input("\n Invalid input. Kindly use the available options. Press enter to continue... ")
                    continue
        if navigate.upper() not in "NPB" and navigate.upper() not in page_options:
                input("\n Invalid input. Kindly use the available options. Press enter to continue... ")
                continue
 
    Menu_Work_log.clear_screen()
    Previous_work_log.show_previous_entries_menu()
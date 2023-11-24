from rebel_data_class import rebel_data
import os

##INITIALISE
boh_data = rebel_data()

##1st WINDOW -- SEARCH MODE
def search_window(boh_data,state):
    os.system('cls||clear')
    while state == "search": 
        print("--- SEARCH MODE ---")
        scan_var = input('Scan now:')
        area = boh_data.search_to_locate(scan_var)
        print('Location: {}\n'.format(area))
        if scan_var == "modify":
            state = "modify"
            os.system('cls||clear')
            break
        elif scan_var =="exit":
            state = scan_var
            print("\n---Updating Data --- Please wait.---\n")
            boh_data.upload_data()
            print("----------Update completed-----------")
            break
    return state

#2nd WINDOW -- MODIFY MODE
def modify_window(boh_data,state):
    os.system('cls||clear')
    user = 1
    new_area_list = []
    while state == "modify":
        os.system('cls||clear')      
        print("--- MODIFY MODE---")
        scan_var = input("Available actions:\n*Add new area\n*Add item in\n*Sub item out\n*Clear area\n*X item in area\n*search\n*exit\nSelect Action: ")
        if scan_var == "Add new area":  #ADD NEW AREA FUNCTION
            os.system('cls||clear')  
            area_name = input("\nNew area name?: ")
            confirm = input("Area name: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                new_area_list = []
                print("\nWhen Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == "finish":
                        break
                    new_area_list.append(bar_scan)
                    boh_data.add_new_area(area_name,new_area_list)
                print("\nCOMPLETED. NEW AREA AVAILABLE\n")
        if scan_var == "Add item in":   #ADD ITEM IN FUNCTION
            os.system('cls||clear') 
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                new_area_list = []
                print("\nWhen Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"ADD")
                print("\nItem/s added in {}".format(area_name))
        if scan_var == "Sub item out":  #SUB ITEM OUT FUNCTION
            os.system('cls||clear')  
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                new_area_list = []
                print("\nWhen Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"SUB")
                print("\nItem/s subbed out of {}".format(area_name))
        if scan_var == "Clear area":
            os.system('cls||clear')  
            area_name = input("\nWhat area?:")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                placeHolder = 0
                boh_data.edit_area(area_name, placeHolder,"CLEAR")
                print("\nCLEARED all items in area: {}".format(area_name))
        if scan_var == "X item":
            os.system('cls||clear')  
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                bar_scan = bar_scan = input('Scan now: ')
                confirm_all = input("Confirm to clear all item with matching barcode with yes or no: ")
                if confirm_all == 'yes':
                    boh_data.edit_area(area_name,bar_scan,"X")
                    print("\nCLEARED all identical barcode in area: {}".format(area_name))
        if scan_var == "search":
            state = scan_var
            print("\n---Updating Data --- Please wait.---\n")
            boh_data.upload_data()
            print("----------Update completed------------\n")
            return state
        if scan_var != 'Add new area' or 'Add item in' or "Sub item out" or 'Clear area' or "X item" or "search" or "exit":
            input("Press enter/scan any barcode to continue\n")
        if scan_var == "exit":
            state = scan_var
            print("\n---Updating Data --- Please wait.---\n")
            boh_data.upload_data()
            print("------------Update completed----------\n")
            return state

def main():
    state = 'search'
    print("OPENING ---------------------------------------------------------------------------------")
    while state == 'search':
        #print(boh_data.data)
        state = search_window(boh_data,state)
        if state == 'modify':
            print(boh_data.data)
            state = modify_window(boh_data,state)
        if state == 'exit':
            print("\n--------------CLOSING ----------------")
            return
## RUNNING MAIN LOOP
main()




    


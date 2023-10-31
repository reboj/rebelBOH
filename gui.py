from rebel_data_class import rebel_data

##INITIALISE
boh_data = rebel_data('dataLoc.csv')


##1st WINDOW -- SEARCH MODE
def search_window(boh_data,state):
    while state == "search":    
        print("--- SEARCH MODE ---")
        scan_var = input('Scan now:')
        area = boh_data.search_to_locate(scan_var)
        print('Location: {}\n'.format(area))
        if scan_var == "modify":
            state = "modify"
            break
        elif scan_var =="exit":
            state = scan_var
            print("---Updating Data -- Please wait.---")
            boh_data.upload_data_csv('dataLoc_update.csv')
            boh_data.update_csv_names('dataLoc.csv','dataLoc_update.csv')
            print("===Update completed===")
            break
    return state

#2nd WINDOW -- MODIFY MODE
def modify_window(boh_data,state):
    user = 1
    new_area_list = []
    while state == "modify":      
        print("--- MODIFY MODE---")
        scan_var = input("Available actions:\n*Add new area\n*Add item in\n*Sub item out\n*Clear area\n*X item in area\n*search\n*exit\nSelect Action: ")
        if scan_var == "Add new area":  #ADD NEW AREA FUNCTION
            area_name = input("Area name: ")
            confirm = input("Area name: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                new_area_list = []
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == "finish":
                        break
                    new_area_list.append(bar_scan)
                    boh_data.add_new_area(area_name,new_area_list)
                print("COMPLETED. NEW AREA AVAILABLE")
        if scan_var == "Add item in":   #ADD ITEM IN FUNCTION
            area_name = input("What area?: ")
            confirm = input("Area: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                new_area_list = []
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"ADD")
                print("Item/s add in {}".format(area_name))
        if scan_var == "Sub item out":  #SUB ITEM OUT FUNCTION
            area_name = input("What area?: ")
            confirm = input("Area: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                new_area_list = []
                while user == 1:
                    bar_scan = input('Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"SUB")
                print("Item/s sub out of {}".format(area_name))
        if scan_var == "Clear area":
            area_name = input("What area?:")
            confirm = input("Area: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                placeHolder = 0
                boh_data.edit_area(area_name, placeHolder,"CLEAR")
                print("CLEAR all completed at {}".format(area_name))
        if scan_var == "X item":
            area_name = input("What area?: ")
            confirm = input("Area: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                bar_scan = bar_scan = input('Scan now: ')
                confirm_all = input("Confirm to clear all item with matching barcode with yes or no: ")
                if confirm_all == 'yes':
                    boh_data.edit_area(area_name,bar_scan,"X")
                    print("CLEAR all items at {}".format(area_name))
        if scan_var == "search":
            state = scan_var
            print("---Updating Data -- Please wait.---")
            boh_data.upload_data_csv('dataLoc_update.csv')
            boh_data.update_csv_names('dataLoc.csv','dataLoc_update.csv')
            print("===Update completed===\n")
            return state
        if scan_var != 'Add new area' or 'Add item in' or "Sub item out" or 'Clear area' or "X item" or "search":
            input("Input any key to continue\n")
        if scan_var == "exit":
            state = scan_var
            print("---Updating Data -- Please wait.---")
            boh_data.upload_data_csv('dataLoc_update.csv')
            boh_data.update_csv_names('dataLoc.csv','dataLoc_update.csv')
            print("===Update completed===")
            return state

def main():
    state = 'search'
    print("OPENING -----\n-------\n----------\n-----------------\n")
    while state == 'search':
        print(boh_data.data)
        state = search_window(boh_data,state)
        if state == 'modify':
            print(boh_data.data)
            state = modify_window(boh_data,state)
        if state == 'exit':
            print("CLOSING ---------------------\n----------------n------")
            return
## RUNNING MAIN LOOP
main()




    


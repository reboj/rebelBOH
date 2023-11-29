from rebel_data_class import rebel_data
import os


##INITIALISE
boh_data = rebel_data()

##1st WINDOW -- SEARCH MODE
def search_window(boh_data,state):
    os.system('cls||clear')
    while state == "search":
        results = [] 
        print("\n -------------------- SEARCH MODE ---------------------\n")
        print(' Scan barcode to search for its area if it exist.\n Access SAP for barcode(GTIN) if needed be.\n Need to use right click of mouse to paste barcode.\n To go to Modify mode; scan/type: modify.') 
        scan_var = input('\n Scan barcode: ')
        print('')
        areas = boh_data.search_to_locate(scan_var)
        if len(areas) == 0:
            print(" NO MATCH IN DATABASE")
        if len(areas) > 0:
            print(' Locations  :Qty\n')
            for area in areas:
                print(' {:<10} :{}'.format(area, areas.get(area)))
        if scan_var == "modify":
            state = "modify"
            os.system('cls||clear')
            break
        elif scan_var =="exit":
            state = scan_var
            print("\n \t---Updating Data --- Please wait.---")
            boh_data.upload_data()
            print(" \t----------Update completed-----------")
            break
        input('\n Scan/type any input to continue.')
        os.system('cls||clear')

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
            print("-ADD NEW AREA-")  
            area_name = input("\nNew area name?: ")
            confirm = input("Area name: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                os.system('cls||clear') 
                print("-ADD NEW AREA-")
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
            print("-ADD ITEM IN-")
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                os.system('cls||clear')
                print("-ADD ITEM IN-")  
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
            print("-SUB ITEM OUT-")  
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                os.system('cls||clear')
                print("-SUB ITEM OUT-")  
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
            area_name = input("\nWhat area to clear?:")
            confirm = input("\nArea to clear: {}. Confirm with yes or no: ".format(area_name))
            if confirm =="yes":
                placeHolder = 0
                boh_data.edit_area(area_name, placeHolder,"CLEAR")
                print("\nCLEARED all items in area: {}".format(area_name))
        if scan_var == "X item":
            os.system('cls||clear')
            print("-X ITEM-")  
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}. Confirm with yes or no: ".format(area_name))
            if confirm == "yes":
                os.system('cls||clear')
                print("-X ITEM-")  
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
            print("\n \t---Updating Data --- Please wait.---")
            boh_data.upload_data()
            print(" \t----------Update completed-----------")
            return state

def main():
    state = 'search'
    #print(boh_data.data)
    while state == 'search':
        #print(boh_data.data)
        state = search_window(boh_data,state)
        if state == 'modify':
            print(boh_data.data)
            state = modify_window(boh_data,state)
        if state == 'exit':
            print(" \t--------------CLOSING ----------------\n")
            return
## RUNNING MAIN LOOP
main()




    


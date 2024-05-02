from rebel_data_class import rebel_data
from pdfgen import print_barcode
from pdfgen import custom_print_barcodes
import os


##INITIALISE
boh_data = rebel_data()

##1st WINDOW -- SEARCH MODE
def search_window(boh_data,state):
    os.system('cls||clear')
    while state == "search":
        results = [] 
        print("\n -------------------- SEARCH MODE ---------------------\n")
        text_01 = ' Scan barcode to search for its area if it exist.\n'
        text_02 = ' Access SAP for barcode(EAN) if needed be.\n'
        text_03 = ' To go to Modify mode; scan/type: modify.'
        print( text_01 + text_02 + text_03) 

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
        print("\n -------------------- MODIFY MODE ---------------------\n")
        text_01 = ' Available Actions:\n\n'
        input_00 = ' ~ Add new area\n'
        input_01 = ' ~ Add item in\n'
        input_02 = ' ~ Sub item out\n'
        input_03 = ' ~ Clear area\n'
        input_04 = ' ~ X item\n\n'
        input_05 = ' ~ Custom print areas\n'
        input_06 = ' ~ search\n'
        input_07 = ' ~ exit\n\n'
        input_08 = ' ~ Transfer\n'
        text_02 = ' Select Action: '
        scan_var = input(text_01 + input_00 +input_01 + input_02 + input_03 + input_04 + input_05 + input_06 + input_07 + text_02)
        

        if scan_var == "Add new area":  #ADD NEW AREA FUNCTION
            os.system('cls||clear')
            print("\n ----------ADD NEW AREA-----------")  
            area_name = input("\n New area name?: ")
            confirm = input(" Area name: {}.\n Confirm with yes or no: ".format(area_name))
            check = boh_data.if_area_exist(area_name)
            if confirm == "yes" and check == False:
                os.system('cls||clear') 
                print("\n ----------ADD NEW AREA-----------")  
                new_area_list = []
                print("\n When Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input(' Scan now: ')
                    if bar_scan == "finish":
                        break
                    new_area_list.append(bar_scan)
                    outcome = boh_data.add_new_area(area_name,new_area_list)
                print_barcode(area_name)
                print("\n COMPLETED. NEW AREA AVAILABLE.")
            if check == True and confirm == 'yes':
                print("\n Area already exist in database. Try Add item in.\n")

        if scan_var == "Add item in":   #ADD ITEM IN FUNCTION
            os.system('cls||clear')
            print("\n ----------ADD ITEM IN AREA-----------")  
            area_name = input("\n What area?: ")
            confirm = input("\n Area: {}.\n Confirm with yes or no: ".format(area_name))
            check = boh_data.if_area_exist(area_name)
            if confirm =="yes" and check == True:
                os.system('cls||clear')
                print("\n ----------ADD ITEM IN AREA-----------")
                if boh_data.items_count(area_name) <= 0:
                    print('\n ~ Area clear. No items inside ~')
                else: print('\n ~ Existing items inside {} ~'.format(area_name))    
                new_area_list = []
                print(" When Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input(' Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"ADD")
                print("\n Item/s added in {}".format(area_name))
            if check == False and confirm == 'yes':
                print("\n No area exist in database. Double check area or add new area.\n")

        if scan_var == "Sub item out":  #SUB ITEM OUT FUNCTION
            os.system('cls||clear')
            print("\n ----------SUB ITEM OUT IN AREA-----------")  
            area_name = input("\nWhat area?: ")
            confirm = input("\nArea: {}.\nConfirm with yes or no: ".format(area_name))
            check = boh_data.if_area_exist(area_name)
            if confirm =="yes" and check == True:
                os.system('cls||clear')
                print("\n ----------SUB ITEM OUT IN AREA-----------")  
                new_area_list = []
                print("\n When Finished. Type/Scan:finish\n")
                while user == 1:
                    bar_scan = input(' Scan now: ')
                    if bar_scan == 'finish':
                        break
                    boh_data.edit_area(area_name,bar_scan,"SUB")
                print("\n Item/s subbed out of {}".format(area_name))
            if check == False and confirm == 'yes':
                print("\n No Area exit in database. Double check area.\n")

        if scan_var == "Clear area":
            os.system('cls||clear')
            print("\n ----------CLEAR AREA-----------")  
            area_name = input("\n What area to clear?:")
            check = boh_data.if_area_exist(area_name)
            if check == True:
                area_count = boh_data.items_count(area_name)
                print(' \n No. of items in {} = {}'.format(area_name,area_count))
                confirm = input("\n Area to clear: {}\n Confirm with yes or no: ".format(area_name))
                if confirm == 'yes':            
                    placeHolder = 0
                    boh_data.edit_area(area_name, placeHolder,"CLEAR")
                    print("\n CLEARED all items in area: {}".format(area_name))
            if check == False:
                print("\n No Area exit in database. Double check area.\n")

        if scan_var == "X item":
            os.system('cls||clear')
            print("\n ---------- X ITEM OUT IN AREA-----------")    
            area_name = input("\n What area?: ")
            confirm = input("\n Area: {}.\n Confirm with yes or no: ".format(area_name))
            check = boh_data.if_area_exist(area_name)
            if confirm == "yes" and check == True:
                os.system('cls||clear')
                print("\n ---------- X ITEM OUT IN AREA-----------\n")    
                bar_scan = bar_scan = input(' Scan now: ')
                count = boh_data.items_in(area_name,bar_scan)
                print('\n {} items with scanned barcode in {}.'.format(count,area_name))
                print('\n Clear all identical barcode in {}?'.format(area_name))
                confirm_all = input(" Confirm with yes or no: ")
                if confirm_all == 'yes':
                    boh_data.edit_area(area_name,bar_scan,"X")
                    print("\n CLEARED all identical barcode in area: {}".format(area_name))
            if check == False and confirm == 'yes':
                print("\n No Area exit in database. Double check area.\n")

        if scan_var == "Custom print areas":
            custom_print = {}
            while user == 1:
                os.system('cls||clear')
                print("\n ---------- Custom Print Areas -----------\n")
                print("\n When finished. Scan/type: finish at Action.\n")
                area = input(" Area Name: ")
                qty = input(" Qty: ")
                print("\n {}-{}. Confirm with yes to print, no to retry.".format(area,qty))
                print(" If finished, scan/type finish. (Confirm yes first, to add the above inputs for printing.)")
                confirm = input("\n Action (yes/no/finish): ")
                if confirm == 'yes':
                    custom_print[area] = int(qty)
                if confirm == 'finish':
                    if len(custom_print) > 0:
                        custom_print_barcodes(custom_print)
                    break
        
        if scan_var == 'Transfer':
            os.system('cls||clear')
            print("\n ---------- TRANSFER -----------")
            print("\n Transfer items from one area to another.")
            from_area = input("\n FROM what area? ")
            to_area = input("\n To which area? ")
            print("\n Transfer items from {} to {}?.".format(from_area,to_area))
            confirm = input(" Confirm with yes or no: ")
            if confirm == 'yes':
                condition = boh_data.change_area(from_area,to_area)
                if condition == True:
                    print("\n Transfer completed from {} to {}.".format(from_area,to_area))
                else:
                    print("\n Transfer failed. One of the areas does not exist.")
            

        if scan_var == "search":
            state = scan_var
            print("\n---Updating Data --- Please wait.---\n")
            boh_data.upload_data()
            print("----------Update completed------------\n")
            return state

        if scan_var != 'Add new area' or 'Add item in' or "Sub item out" or 'Clear area' or "X item" or "search" or "exit":
            input(" Press enter/scan any barcode to continue.\n")

        if scan_var == "exit":
            state = scan_var
            print("\n \t---Updating Data --- Please wait.---")
            boh_data.upload_data()
            print(" \t----------Update completed-----------")
            return state
        
        boh_data.upload_data()
        
        


def main():
    state = 'search'
    #print(boh_data.data)
    while state == 'search':
        #print(boh_data.data)
        state = search_window(boh_data,state)
        if state == 'modify':
            #print(boh_data.data)
            state = modify_window(boh_data,state)
        if state == 'exit':
            print(" \t--------------CLOSING ----------------\n")
            return
## RUNNING MAIN LOOP
if __name__ == '__main__':
    main()  




    


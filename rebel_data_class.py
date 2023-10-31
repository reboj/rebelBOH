#RebelBOH class
import pickle 
import csv
import os

class rebel_data():
    def __init__(self,csv_file):
        with open("bohData.pkl","rb") as d_file:
            self.data = pickle.load(d_file)
            
    def add_new_area(self, area_name,items_list):
        self.data.update({area_name:items_list})    
        return 
    
    def edit_area(self, area_name,scanned_item,action):
        items_inside = self.data.get(area_name)
        items_count = len(items_inside)
        new_list = []

        if action == 'ADD':   #ADD ITEM --TESTED
            items_inside.append(scanned_item)
            self.data[area_name] = items_inside
        elif action == 'SUB':     #SUB ITEM --TESTED
            items_inside.remove(scanned_item)
            self.data[area_name] = items_inside
        elif action == 'CLEAR':     #CLEARS AREA --TESTED
            items_inside = []
            self.data[area_name] = items_inside
        elif action == 'X':      #SUB ITEM COMPL --TESTED
            for i in range(items_count):
                if items_inside[i] != scanned_item:
                    new_list.append(items_inside[i])
            self.data[area_name] = new_list
        else:             #NO ACTION     
            self.data[area_name] = items_inside

        return 


    # SEARCH SCANNED ITEM IN DATABASE -- TESTED     
    def search_to_locate(self,scanned_item):
        scan_condition = False
        for areas, items in self.data.items():
            for item in items:
                if item == scanned_item:
                    scan_condition = True
                    return areas
    
        if scan_condition == False:
            return print("NO MATCH")

    def upload_data_csv(self,new_csv_file): # --TESTED
        fieldnames = self.data.keys()
        with open(new_csv_file,'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(self.data)
        with open ("bohData.pkl","wb") as s_file:
            pickle.dump(self.data,s_file)
        return
    
    def update_csv_names(self,old_name,new_name):
        if os.path.exists(old_name):
            os.remove(old_name)
            os.rename(new_name,old_name)
        else:
            print("FILE NOT FOUND -- FAILED ACTION")
        return
        







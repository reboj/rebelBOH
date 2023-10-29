#RebelBOH class

import pandas as pd 
import numpy as np
import csv

class rebel_data():
    def __init__(self,csv_file):
        self.data = pd.read_csv(csv_file,index_col=False)
        self.data = pd.DataFrame.to_dict(self.data, orient='series')
        for areas, items in self.data.items():
            value_list = pd.Series.to_list(self.data.get(areas))
            self.data[areas] = value_list
    
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

#<FUNCTION IMPLEMENTATION EXAMPLE>
#boh_data = rebel_data('dataLoc.csv')
#boh_data.add_new_area('a6',[123,123,4356])
#boh_data.edit_area('a1',"TESTINPUT","ADD")
#site = boh_data.search_to_locate(123)
#boh_data.upload_data_csv('dataLoc_update.csv')
###########################################





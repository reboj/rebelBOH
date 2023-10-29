## REBEL BOH
## I need a set function to convert og. dict values by pd.series.tolist()

import pandas as pd
import numpy as np
import csv

#IMPORT CSV DATA TO PYTHON DICT
boh_data = pd.read_csv('dataLoc.csv', index_col=False)
boh_data = pd.DataFrame.to_dict(boh_data, orient='series')

def init_values(data):
    for areas, items in data.items():
        value_list = pd.Series.tolist(data.get(areas))
        data[areas] = value_list
    return data
        
#ADD NEW "AREAS AND ITEMS" TO DICT --TESTED
def add_new_area(data, area_name,items_list):
    data.update({area_name:items_list})    
    return data

#MODIFY DATA
def edit_area(data, area_name,scanned_item,action):
    items_inside = data.get(area_name)
    items_count = len(items_inside)
    new_list = []

    if action == 'ADD':   #ADD ITEM --TESTED
        items_inside.append(scanned_item)
        data[area_name] = items_inside
    elif action == 'SUB':     #SUB ITEM --TESTED
        items_inside.remove(scanned_item)
        data[area_name] = items_inside
    elif action == 'CLEAR':     #CLEARS AREA --TESTED
        items_inside = []
        data[area_name] = items_inside
    elif action == 'X':      #SUB ITEM COMPL --TESTED
        for i in range(items_count):
            if items_inside[i] != scanned_item:
                new_list.append(items_inside[i])
        data[area_name] = new_list
    else:               #NO ACTION
        data[area_name] = items_inside

    return data


# SEARCH SCANNED ITEM IN DATABASE -- TESTED
def search_to_locate(data,scanned_item):
    scan_condition = False
    for areas, items in data.items():
        for item in items:
            if item == scanned_item:
                scan_condition = True
                return areas
    
    if scan_condition == False:
        return print("NO MATCH")

def upload_data_csv(data): # --TESTED
    fieldnames = data.keys()
    with open('dataLoc_update.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
    

#MAIN LOOP
boh_data = init_values(boh_data)

boh_data = add_new_area(boh_data,"a5",[3456,1234,3456])
boh_data = edit_area(boh_data,"a1","TEST","ADD")
area = search_to_locate(boh_data,"TEST")

upload_data_csv(boh_data)



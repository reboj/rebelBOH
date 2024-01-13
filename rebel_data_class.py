#RebelBOH class
import pickle


class rebel_data():
    def __init__(self):
        with open("bohData.pkl","rb") as d_file:
            self.data = pickle.load(d_file)

    def if_area_exist(self,area_name):
        if area_name in self.data.keys():
            return True
        else:
            return False
        
    def add_new_area(self, area_name,items_list):
        self.data.update({area_name:items_list})
        return True
    
    def edit_area(self, area_name,scanned_item,action):
        items_inside = self.data.get(area_name)
        items_count = len(items_inside)
        new_list = []
        count = 0

        if action == 'ADD':   #ADD ITEM --TESTED
            items_inside.append(scanned_item)
            self.data[area_name] = items_inside

        elif action == 'SUB':
            for item in items_inside:
                if scanned_item in items_inside:
                    count = items_inside.count(scanned_item)
            if count >= 1:
                items_inside.remove(scanned_item)
                self.data[area_name] = items_inside
                if count >= 0:
                    count = count - 1
                print(' New QTY: {}'.format(count))
            else:
                print(" QTY: 0 in this area.\n")  

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
        area_list = {}
        scan_condition = False
        for areas, items in self.data.items():
            for item in items:
                if item == scanned_item:
                    if areas in area_list:
                        area_list[areas] += 1
                    else:
                        area_list[areas] = 1
                    scan_condition = True
        return area_list
    
    def upload_data(self): # --TESTED
        with open ("bohData.pkl","wb") as s_file:
            pickle.dump(self.data,s_file)
        return
    
    def items_count(self,area_name):
        items_inside = self.data.get(area_name)
        items_count = len(items_inside)
        return items_count
    
    def items_in(self,area_name,bar_scan):
        count = 0
        items_inside = self.data.get(area_name)
        for item in items_inside:
            if bar_scan == item:
                count = count + 1
        return count









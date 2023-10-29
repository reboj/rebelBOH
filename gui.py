from rebel_data_class import rebel_data



#<FUNCTION IMPLEMENTATION EXAMPLE>
boh_data = rebel_data('dataLoc.csv')
boh_data.add_new_area('a6',[123,123,4356])
boh_data.edit_area('a1',"NEWESTINPUT3","CLEAR")
site = boh_data.search_to_locate("NEWESTINPUT3")
print(site)
#boh_data.upload_data_csv('dataLoc_update.csv')
#boh_data.update_csv_names('dataLoc.csv','dataLoc_update.csv')



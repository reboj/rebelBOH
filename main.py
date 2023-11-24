##CUSTOMTKINTER implementation
import customtkinter as ctk 
import tkinter as tk
from rebel_data_class import rebel_data

#Initialize
boh_data = rebel_data()

#Functions
def modify_mode():
    main_label.configure(text="--- Modify Mode ---")
    modify_text = 'Scan/type the available actions:\n*Add new area\n*Add item in\n*Sub item out\n*Clear Area\n*X item\n*search\n*exit'
    info_label.configure(text=modify_text)
    return

def search_mode(event):
    if scanned_var.get() == 'modify':
        modify_mode()
    area = boh_data.search_to_locate(scanned_var.get())
    output_var.set(area)
    return


#Window -- BASE
window = ctk.CTk()
window.title("rebelBOH RHTC")
window.geometry("1300x1200")
ctk.set_appearance_mode("dark")
#Widgets
main_label = ctk.CTkLabel(window, text="--- Search Mode ---",font=('calibri',60))
main_label.pack(pady=100)

info_text = 'Scan barcode to search for its area if it exist.\nAccess SAP for barcode(GTIN) if needed be.\nTo go to Modify mode; scan/type: modify.'
info_label = ctk.CTkLabel(window, text=info_text, font=('ariel',40))
info_label.pack()

scanned_var = tk.StringVar()
search_bar = ctk.CTkEntry(window,textvariable=scanned_var,width=800,height=50,font=('ariel',30))
search_bar.bind('<Return>',search_mode)
search_bar.pack(pady=80)
search_bar.focus()

output_var = tk.StringVar()
output_label = ctk.CTkEntry(window, textvariable=output_var, font=('ariel',100),width=985,fg_color='transparent')
output_label.pack(pady=50)

#Main Loop
window.mainloop()

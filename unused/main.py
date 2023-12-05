##CUSTOMTKINTER implementation
import customtkinter as ctk 
import tkinter as tk
from rebel_data_class import rebel_data

#Initialize
boh_data = rebel_data()
ctk.set_appearance_mode("dark")

def search_mode(event):
    if scanned_var.get() == 'modify':
        modify_mode()
    area = boh_data.search_to_locate(scanned_var.get())
    output_var.set(area)
    return


#Window -- BASE
search_window = ctk.CTk()
search_window.title("rebelBOH RHTC")
search_window.geometry("1300x1200")

#Widgets
main_label = ctk.CTkLabel(search_window, text="--- Search Mode ---",font=('calibri',60))
main_label.pack(pady=100)

search_info_text = 'Scan barcode to search for its area if it exist.\nAccess SAP for barcode(GTIN) if needed be.\nTo go to Modify mode; scan/type: modify.'
search_info = ctk.CTkLabel(search_window, text=search_info_text, font=('ariel',40))
search_info.pack()

scanned_var = tk.StringVar()
search_bar = ctk.CTkEntry(search_window,textvariable=scanned_var,width=800,height=50,font=('ariel',30))
search_bar.bind('<Return>',search_mode)
search_bar.pack(pady=80)
search_bar.focus()

output_var = tk.StringVar()
output_label = ctk.CTkLabel(search_window, textvariable=output_var, font=('ariel',100),width=985,fg_color='transparent')
output_label.pack(pady=50)

#Main Loop
search_window.mainloop()



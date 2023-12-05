## GUI CLASS
import tkinter as tk 
from tkinter import ttk
from rebel_data_class import rebel_data

#Initialize
boh_data = rebel_data()

#Functions
def search_mode(event):
    area = boh_data.search_to_locate(search_bar_var.get())
    output_var.set(area)
    return
    
       
#Window
window = tk.Tk()
window.title('rebelBOH RHTC')
window.geometry('1500x1200')

#Widgets
title_label = ttk.Label(master=window, text='--- Search Mode ---', font='ariel 20 bold')
title_label.pack(pady=100)

des_text = 'Scan barcode to search for its area if it exist.\nAccess SAP for barcode(GTIN) if needed be.\nTo go modify mode, scan/type: modify'
description = ttk.Label(master=window, text=des_text, font='ariel 10')
description.pack()

#Input field -- Search Window
input_frame = ttk.Frame(master=window)
input_frame.pack(pady=20)

search_bar_var = tk.StringVar()
search_bar = ttk.Entry(master=input_frame, textvariable=search_bar_var)
search_bar.bind('<Return>', search_mode)
search_bar.pack(side='left')
search_bar.focus()

output_var = tk.StringVar()
output_label = ttk.Label(master=window,text='output',font='ariel 30 bold', textvariable=output_var)
output_label.pack(pady=150)

#Main
window.mainloop()


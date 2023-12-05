##CUSTOMTKINTER implementation
import customtkinter as ctk 
import tkinter as tk
from rebel_data_class import rebel_data

#Initialization
boh_data = rebel_data()
ctk.set_appearance_mode("dark")

#Class
class gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('rebelBOH RHTC')
        self.geometry('1300x1200')
        self.main_label_text = ''
        self.main_label = ctk.CTkLabel(self, text=self.main_label_text,font=('calibri',60))
        

#Main Loop
window = gui()
window.main_label.configure("Main Label")
window.main_label.pack()
window.mainloop()

from barcode import Code128 
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os.path
import os
import sys
import subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def print_barcode(area_name):
    options = {
    'module_width': 0.2,
    'module_height': 10.0,
    'quiet_zone': 20.0,
    'font_size': 30,
    'text_distance': 14.0}

    barcode_folder = 'barcodes/'  
    pdf_filename = 'barcodes.pdf'
    
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    text_barcode = Code128(area_name, writer=ImageWriter())
    barcode_filename = barcode_folder + area_name
    text_barcode.save(barcode_filename, options=options)

    c.drawInlineImage(barcode_filename + '.png', -50, -100)
    c.showPage()
    c.save()
    #os.startfile('barcodes.pdf')
    open_file('barcodes.pdf')
    
def custom_print_barcodes(areas_dict):
    #os.startfile('barcodes.pdf')
    areas_to_print = []
    options = {
    'module_width': 0.2,
    'module_height': 10.0,
    'quiet_zone': 20.0,
    'font_size': 30,
    'text_distance': 14.0}

    barcode_folder = 'barcodes/'  
    pdf_filename = 'barcodes.pdf'
    
    c = canvas.Canvas(pdf_filename, pagesize=letter)


    for key in areas_dict:
        for count in range(areas_dict.get(key) + 1 ):
            if count > 0:
                areas_to_print.append('{}-{}'.format(key,count))
    
    for text in areas_to_print:
        text_barcode = Code128(text, writer=ImageWriter())
        barcode_filename = barcode_folder + text
        text_barcode.save(barcode_filename, options=options)

        c.drawInlineImage(barcode_filename + '.png', -50, -100) 
        c.showPage()   
    c.save()
    #os.startfile('barcodes.pdf')
    open_file('barcodes.pdf')



#texts = ['A-21','dcb-15']


#options = {
    #'module_width': 0.2,
   # 'module_height': 10.0,
    #'quiet_zone': 20.0,
   # 'font_size': 30,
    #'text_distance': 14.0
#}
#barcode_folder = 'barcodes/'  
#pdf_filename = 'barcodes.pdf'

# Create a PDF file
#c = canvas.Canvas(pdf_filename, pagesize=letter)

#for text in texts:
    # Generate and save the barcode image
   # text_barcode = Code128(text, writer=ImageWriter())
   # barcode_filename = barcode_folder + text
   # text_barcode.save(barcode_filename, options=options)

    # Draw the barcode image on the PDF
   # c.drawInlineImage(barcode_filename + '.png', -50, -100)  # Adjust the coordinates as needed

    # Move to the next page for the next barcode
   # c.showPage()

# Save the PDF file
#c.save()











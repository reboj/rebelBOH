from barcode import Code128 
from barcode.writer import ImageWriter
# DOCS -- options: https://python-barcode.readthedocs.io/en/stable/writers.html#common-writer-options


texts = ['A-21']
options = {'module_width':0.2,
            'module_height':10.0,
            'quiet_zone':20.0,
            'font_size':30,
            'text_distance':14.0
           }
barcode_folder = 'barcodes/'  

#for text in texts:
    #text_barcode = Code128(text,writer=ImageWriter())         
   # text_barcode.save(barcode_folder + text, options)



    

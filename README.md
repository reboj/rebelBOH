# rebelBOH
Back-Of-House(BOH) database app 

**Project Overview**
Creation of BOH database app to quickly and accurately locate stored products at BOH. 
The app's database is built upon Python for faster and scalable approach as database gets larger. 

The store is partitioned into different areas like stocktake. By adding new areas into the app’s database with its respective items, 
the app’s search window will be able to search the scanned barcode and call out its respective areas alongside the item’s quantity. 
While the modify window will allow users to modify the app’s database to reflect current stock locations. 

The app is designed to be used single-handedly with a barcode scanner for the intentions of efficient workflow. Every action needed to operate the app will have its own barcode thereby users are to follow the prompts displayed on the app’s interface and simply scan the barcode of the desired action. Moreover, typing the inputs can be done by users however users need to be cautious of white spaces and capital letters when typing. The correct typography for typed inputs is displayed on the app’s interface.


**App Overview**
* 'Search/Locate' tab. 
  Functions:
  -> End user inputs product's barcode either by typing or by scanning which leads to output the name of location.

* 'Modify' tab.
  Functions:
  -> Add new areas and corresponding contents.
  -> Modify existing area's contents.
  -> Delete existing areas and corresponding contents.

* 'Communication' tab.
  Functions:
  -> Allows end users to record or place notes for communication to others.

**FEEDBACK as of Nov 6, 2023**
* Running terminal/command prompt interface could lead to confusion to other team members -- Yoong, Josh, Jenn.
R: Adding Guided User Interface (GUI).
* Code needs to be more resilant with wrong inputs -- Rebo, Jenn.
R: Add an extra funciton for wrong inputs.
* Opening the 'app' through command prompt could be more accessible. -- Rebo
R: Create script file to run gui.py from destop python file.
* How to tell if an area exist already. -- Tamara
R: Remove case sensistivity. Then create function to identify if an area already exist.
* To be able to tell if an item scanned has been scanned under multiple areas -- Jason
R: Display all areas where there is matching barcode. 



  





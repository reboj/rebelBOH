# rebelBOH
Back-Of-House(BOH) database app 

**Project Overview**
Creation of BOH database app to quickly and accurately locate stored products at BOH. 
The app's database is built upon Python for faster and scalable approach as database gets larger. 


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



  





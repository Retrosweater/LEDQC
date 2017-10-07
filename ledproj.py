import tkinter as tk; #Tkinter for canvas
from msvcrt import getch; #Getch for keypresses
import sys;

#Input and error handling
while True:	#Tile Width input
	try:
		tilewidth = int(input('Enter tile width: '))
		if tilewidth > 250:
				print("Invalid tile width!")
				continue
	except ValueError:
		print("Invalid Entry, Russell.")
		continue
	else:
		break

while True: #Tile Height input
	try:
		tileheight = int(input('Enter tile height: '))
		if tileheight > 250:
				print("Invalid tile height!")
				continue
	except ValueError:
		print("Invalid Entry, Russell.")
		continue
	else:
		break

while True: #Tile Columns input
	try:
		tilecolumn = int(input('Enter amount of tile columns: '))
		if tilecolumn > 50:
				print("Invalid amount of columns!")
				continue

	except ValueError:
		print("Invalid Entry, Russell.")
		continue
	else:
		break		
		
while True: #Tile Rows input
	try:
		tilerow = int(input('Enter amount of tile rows: '))
		if tilerow > 50:
				print("Invalid amount of rows!")
				continue
	except ValueError:
		print("Invalid Entry, Russell.")
		continue
	else:
		break

totalheight = (tileheight * tilerow)
totalwidth = (tilewidth * tilecolumn)
print('Total resolution is: ', totalwidth, ' x ', totalheight)

##SETUP##
master = tk.Tk()
master.configure(background = 'black')
master.wm_attributes("-topmost", 1)
master.overrideredirect(1)
inv = False
run = 1
global bgcan
bgcan = tk.Canvas(master, width=totalwidth, height=totalheight, bd=0, highlightthickness=0, relief='ridge',)
bgcan.pack()
##SETUP##
   
def checkered(bgcan, line_distanceW, line_distanceH):
   bgcan.config(background="black")
   bgcan.create_line(0, 0, totalwidth, 0, fill= "white")
   bgcan.create_line(0, 0, 0, totalheight, fill= "white")
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distanceW,totalwidth,line_distanceW):
      bgcan.create_line(x, 0, x, totalheight, fill= "white")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distanceH,totalheight,line_distanceH):
      bgcan.create_line(0, y, totalwidth, y, fill = "white")
   # vertical lines at an interval of "line_distance" pixel
   for x in range((line_distanceW - 1),totalwidth,line_distanceW):
      bgcan.create_line(x, 0, x, totalheight, fill = "white")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range((line_distanceH - 1),totalheight,line_distanceH):
      bgcan.create_line(0, y, totalwidth, y, fill = "white")
	 

	  
def invcheckered(canvas, line_distanceW, line_distanceH):
   bgcan.config(background="white")
   bgcan.create_line(0, 0, totalwidth, 0, fill= "black")
   bgcan.create_line(0, 0, 0, totalheight, fill= "black")
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distanceW,totalwidth,line_distanceW):
      bgcan.create_line(x, 0, x, totalheight, fill= "black")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distanceH,totalheight,line_distanceH):
      bgcan.create_line(0, y, totalwidth, y, fill = "black")
   # vertical lines at an interval of "line_distance" pixel
   for x in range((line_distanceW - 1),totalwidth,line_distanceW):
      bgcan.create_line(x, 0, x, totalheight, fill = "black")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range((line_distanceH - 1),totalheight,line_distanceH):
      bgcan.create_line(0, y, totalwidth, y, fill = "black")

	  
checkered(bgcan, tilewidth, tileheight)

def key(event):
	print("Inverting...")
	global inv
	global run
	bgcan.delete("all")
	while run > 0:
		if inv == False:
			invcheckered(bgcan, tilewidth, tileheight)
			inv = True
			print("Inverted.")
			break
		if inv == True:
			inv == True
			checkered(bgcan, tilewidth, tileheight)
			inv = False
			print("Inverted.")
			break
		else:
			break

def key1(event):
	sys.exit(0)

master.bind("a", key) #bind keypress to a
master.bind("q", key1) #bind keypress to q
bgcan.focus_force()

tk.mainloop() #Avoids program end
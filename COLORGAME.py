# import the modules 
from tkinter  import*
import random

root = Tk() 
root.title("COLORGAME") 
root.geometry("1300x700") 
root.resizable(0,0)

# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 'Yellow','Orange','White','Purple','Brown'] 
score = 0

timeleft = 60

# function that will start the game. 
def startGame(event): 
	
	if timeleft ==60: 
		
		# start the countdown timer. 
		countdown() 
		
	# run the function to 
	# choose the next colour.
	
	nextColour() 
        
# Function to choose and 
# display the next colour. 
def nextColour(): 

	# use the globally declared 'score' 
	# and 'play' variables above. 
	global score 
	global timeleft 

	# if a game is currently in play 
	if timeleft > 0: 

		# make the text entry box active. 
		e.focus_set()

		
		# if the colour typed is equal 
		# to the colour of the text 
		if e.get().lower() == colours[1].lower(): 
			
			score += 1

		# clear the text entry box. 
		e.delete(0,END) 
		
		random.shuffle(colours) 
		
		# change the colour to type, by changing the 
		# text _and_ the colour to a random colour value 
		label.config(fg = str(colours[0]), text = str(colours[1])) 
		
		# update the score. 
		scoreLabel.config(text = "Score: "
                                  + str(score)) 
               

# Countdown timer function 
def countdown(): 

	global timeleft 

	# if a game is in play 
	if timeleft > 0: 

		# decrement the timer. 
		timeleft -= 1
		
		# update the time left label 
		timeLabel.config(text = "Time left: "+ str(timeleft)) 
								
		# run the function again after 1 second. 
		timeLabel.after(1000, countdown) 

'''def loop():
        global score
        global timeleft
        if score<=5'''
# Driver Code 

def nextfunc():
        #startGame()
        nextColour()
        countdown()

instructions = Label(root, text = "Type in the colour of the words, and not the word text!",font = ('Helvetica', 12))
instructions.pack() 

scoreLabel = Label(root, text = "Press enter to start", font = ('Helvetica', 12)) 
scoreLabel.pack() 

# add a time left label 
timeLabel = Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 12)) 
				
timeLabel.pack() 

# add a label for displaying the colours 
label = Label(root, font = ('Helvetica', 60)) 
label.pack() 

e = Entry(root) 

# run the 'startGame' function 
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 

# set focus on the entry box 
e.focus_set()

btn=Button(root,text="next",command=nextfunc).place(x=500,y=350)

# start the GUI

root.mainloop() 

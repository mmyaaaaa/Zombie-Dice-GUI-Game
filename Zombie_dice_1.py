# Name: Mya Hussain
# Date: 2018-06-15
# filename: Programming assignment Unit #6
# Description: program runs the game zombie dice in a GUI environment 
# Test cases: Program runs successfully, displays instructions and checks all user input 
# frame classes switch properly, and all functions run on corresponding buttons  
# game behaves as per the instructions and ends upon a winner being declared 

#Import modules  
from tkinter import * 
from tkinter import messagebox
import random 


#Variables needed globally 
names = []
scores = []
who = 0 
scorelabels = []
winner = ""
tempbrain = 0
tempshotgun = 0 
set = []
brainstowin = 13 


#Class that creates a tkinter object 
class mainpage(Tk):   

    #declare a constructor to create an instance/object for this class 
    def __init__(self, *args, **kwargs):
        #this object is the GUI window created below, 
        #this is called via the 'self' keyword referring to the object of x instance
        Tk.__init__(self, *args, **kwargs)

        #set basic properties for window 
        self.title("Zombie Dice")
        self.geometry("1151x756")

        #Make and place a frame using pack, put the frame in the window 
        #let the frame take the shape of the window by expanding and filling
        container = Frame(self)
        container.pack(side = "top", fill ="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #make a dictionary of frame objects to store different pages
        self.frames = {}

        #For each frame (page) put it in the container and add it to the dict
        for every_frame in (startpage, instructions, gameframe, player):

            #make an instance of each frame using the constructor 
            frame = every_frame(container, self)

            #add frame to the list under its name 
            self.frames[every_frame] = frame 

            #put the frame on the application window 
            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        # __init__ is run when program launches thus, 
        # initialize the page shown to startpage
        self.show_frame(startpage)

    #This function raises a given frame 
    #This will create the illusion of new pages and tabs by raising frames
    def show_frame(self, framename ):
        #store the frame to be raised in a variable
        frame = self.frames[framename]
        #raise the frame to make it visible to user vis tkraise method
        frame.tkraise()
 

class startpage(Frame):

    #Make a frame inside the controller
    def __init__(self, parent, controller):

        #Make the frame, the frame is self 
        Frame.__init__(self, parent)
        self.config()
            
        #create canvas for background image 
        can = Canvas(self, width = 1151, height = 756)
        can.place(x = 0, y = 0)

        #put in background image
        self.background = PhotoImage(file = "Zombie Dice! (1).gif")
        self.llabel = Label(can, image = self.background)
        self.llabel.place(x = 0, y = 0)
        

        #make play game and instructions button
        play = Button(can, text= "Click to PLAY", font = "arial 30",\
           bg = "#20b2aa", command = lambda:controller.show_frame(player))

        play.place(x = 100, y = 350)

        instructionbutton = Button( can, text = "INSTRUCTIONS", font = \
            "arial 30", bg ="#ffff99", \
            command = lambda:controller.show_frame(instructions))

        instructionbutton.place(x = 300, y = 450)


#instruction frame accessed from startpage
class instructions(Frame):

    #Make a frame inside the controller
    def __init__(self, parent, controller):
        #Make the frame, the frame is self 
        Frame.__init__(self, parent)
        self.config(bg = "darkblue")

        self.instruct = PhotoImage(file = "Instructions_ (1).gif")
              
        #add a label 
        label = Label(self, image = self.instruct )
        label.place(x = 0, y = 0)

        #Make a back button and place it 
        back = Button(self, text = "Click To Go Back", font = "Ariel 15",\
           bg = "pink", command = lambda:controller.show_frame(startpage))
        back.place( x = 932, y = 680)              
        

#frame that collects the number of players from the user 
class player(Frame):

    #Make a frame inside the controller
    def __init__(self, parent, controller):
        #Make the frame, the frame is self 
        Frame.__init__(self, parent)
        self.config(bg = "brown")

        #background image 
        self.background = PhotoImage(file = "numplayerbackground.gif")
        self.llabel = Label(self, image = self.background)
        self.llabel.place(x = 0, y = 0)

        #entry box for number of players 
        self.numplayers = Entry(self, width = 5)
        self.numplayers.place(x = 720, y = 248)

        #button for entrybox
        self.entrybutton = Button(self, text = "Click to Submit", \
           fg = "red", command = lambda:self.getplayers())
        self.entrybutton.place(x = 775, y = 245)
        
    #this is a function that gets the names of the players depending on how many
    #creates x labels, entryboxes and buttons accordingly 
    def getplayers(self):
        #global variables
        global names 
        global numofplayers

        #check to see if user entered number if not messagebox and stop
        integer = False
        try: 
            numofplayers = int(self.numplayers.get())
            integer = True
        except: 
            messagebox.showerror("Invalid input", "The input must be an integer")

        #check the range of the integer 
        if (integer):
            if (numofplayers <=1):
                messagebox.showerror("Too little players", \
                    "You need at least 2 players to play this game")
            elif (numofplayers > 8):
                messagebox.showerror("Too many players", \
                    "It's recommended no more than 8 people play per game")

            #if between 2 and 8 inclusively get names 
            else: 

                def nothing():
                    messagebox.showerror("Action complete", \
                        "You have already selected the number of players")

                #disable the player button as they no longer need it 
                self.entrybutton.config(command = nothing)

                #store the entryboxes in this list to access later 
                entryboxes = []
                #this is to change the placement of the boxes 
                space = 0

                #for every player make a label and box 
                for p in range(1, numofplayers+1):
                    #Make the needed number of labels 
                    words = "Player " + str(p) +"'s name:"
                    label = Label(self, text = words)
                    label.place( x = 300, y = 315 + space)

                    #Make a corresponding entrybox,
                    #store this entrybox in a list to access later 
                    entryboxes.append(Entry(self, width = 20))
                    entryboxes[p-1].place(x = 400, y = 315 + space)

                    #Increment the space between the items 
                    space += 30

                #make a label and entry box for how many brains to win 
                self.howmany = Label(self, text = "Enter how many \n brains to win:",\
                   font = "ariel 15")
                self.howmany.place(x = 550, y = 315)
                
                self.many = Entry(self)
                self.many.place( x = 720, y = 347)

                #This function gets the value of each entrybox (name)
                #when the start button is pressed
                def getnames ():
                    global names 
                    global numofplayers
                    global brainstowin 

                    #For every player get their name from the entry box
                    # and store it in a list
                    for x in range(numofplayers):
                        try: 
                            #If the entrybox is empty alert user and clear list
                            if entryboxes[x].get().strip() == "":
                                messagebox.showerror("Invalid name",\
                                   "You must fill out all names for each player")
                                names = []
                                break

                            else:
                                #If the name is there add it to the list
                                names.append(entryboxes[x].get())
                        
                        except:
                            #If one name is wrong clear the whole list
                            messagebox.showerror("Invalid name", \
                                "You must fill out all names for each player")
                            names = []
                            break

                    print(numofplayers)     
                    print(names)

                    #check for number to win entry 
                    check = True 
                    while check: 
                        try: 
                            brainstowin = int(self.many.get())

                            if brainstowin <5 or brainstowin >50:
                                messagebox.showerror("Brains to win range", \
                                    "It's recommended you keep the brains\
                                   to win under 50 and over 5")
                                brainstowin = 13 
                                names = []
                                break

                            else:
                                check = False
                        except:
                            
                            messagebox.showerror("Invalid number", \
                                "The number of brains to win must be an " + \
                                "integer")
                            brainstowin = 13
                            names = []
                            break

                    
                    print(brainstowin)
                    #Start the game by going to the gamepage 
                    #Only do this if the list was entered correctly 
                    if (len(names) != 0) and check == False: 
                        mainpage.show_frame(app, gameframe)

                #Make a done button 
                done = Button(self, text = "PRESS TO CONTINUE",\
                   font = "ariel 15", bg = "#870014", fg = "white",\
                  command = getnames)

                done.place(x = 650, y = 510)


#frame where the main game is displayed
class gameframe(Frame):
    global names
    global numofplayers
    global who 
    global scorelabels
    global brainstowin
    global winner

    #Make a frame inside the controller
    def __init__(self, parent, controller):
        #Make the frame, the frame is self 
        Frame.__init__(self, parent)
        self.config(bg = "brown")

        #add background 
        self.background = PhotoImage(file = "backgroundmain.gif")
        self.llabel = Label(self, image = self.background)
        self.llabel.place(x = 0, y = 0)

        #roll the dice button 
        self.rollplz = Button(self, text = "CLICK TO ROLL \n THE DICE",\
           font = "Ariel 20", bg = "#fb4141", command = self.roll)
        self.rollplz.place(x = 85, y = 540)

        #brain label counter
        self.brainlabel = Label(self, text = 0, font = "Ariel 30")
        self.brainlabel.place(x = 680, y = 242) 
        
        #shotgun image counter 
        self.shotgunlabel = Label(self, text = '0', font = "Ariel 30")
        self.shotgunlabel.place(x = 342, y = 242)

        #rolled dice displays  
        self.dice1 = Label(self, bg = "white")
        self.dice1.place(x = 295, y = 358)

        self.dice2 = Label( self, bg = "white")
        self.dice2.place(x = 445, y = 358)

        self.dice3 = Label(self, bg = "white")
        self.dice3.place(x = 600, y = 358)

        #make a list of labels to edit 
        self.labellist = [self.dice1, self.dice2, self.dice3]

        #use canvas to make button to trigger labels 
        #write welcome panel on canvas 
        self.background1 = PhotoImage(file = "welcome to zombie dice.gif")
        self.ccan = Canvas(self, width = 1151 , height = 756)
        self.ccan.place(x = 0, y = 0)
        #put label to put image on canvas 
        self.back = Label(self.ccan, image = self.background1)
        self.back.place(x = 0, y = 0)

        #next button to remove canvas and place names on gameframe 
        nextbutton = Button(self.ccan, text = "NEXT", font = "Ariel 20",\
           bg = "#cb7aed",command = self.writename)
        nextbutton.place(x = 820, y = 575)

    #write out names, make order, declare turns, initialize scores
    def writename(self):
        global names
        global numofplayers
        global scores
        global scorelabels

        #destroy canvas
        self.ccan.destroy()

        #fill up the score list for each player
        #everyone starts with a score of 0 
        for x in names:
            scores.append(0)

        #print the names out in a random playing order on the gamepage 
        if len(names) != 0:
            random.shuffle(names)
            s = 0
            for x in range(len(names)):
                #change font depending on how long the name is 
                if len(names[x]) > 10:
                    f = "Ariel 20"

                else:
                    f = "Ariel 25"
                
                #print name
                self.name = Label(self, text = names[x], font = f)
                self.name.place(x = 855, y = 205+ s)
                
                #print score beside it 
                self.score = Label(self, text = scores[x], \
                    font = "ariel 25" )
                self.score.place(x = 1090, y = 205 +s)
                scorelabels.append(self.score)

                s += 50

            #box for player turn 
            self.turn = Label(self, text = str(names[who]) + "'s Turn", \
                font = "ariel 40", bg = "black", fg = "white",\
               borderwidth = 2, relief = "ridge")
            self.turn.place(x = 440, y = 20)

    def roll (self):
        #this function choses and removes 3 dice from the bag
        def choosedice ():
            global set
            #Chooses three dice and removes them from the bag
            diceinhand = []
            for x in range(3):
                #Try to get three dice
                try: 
                    random.shuffle(set)
                    diceinhand.append(set[len(set)-1])
                    set.pop(len(set)-1)

                #If no dice left, tell user
                #and reset bag to draw from  
                except: 
                    messagebox.showinfo("No Dice", "There are not " + \
                    "enough dice in the bag to draw from as you have " +\
                   "taken out 11 or more dice, all dice shall be " + \
                   "returned to the bag")

                    diceinhand = []
                    set = fulldicebag()
                    for d in range (3):
                        random.shuffle(set)
                        diceinhand.append(set[len(set)-1])
                        set.pop(len(set)-1)
                    break

            #return the rolled dice and the new bag of dice 
            return diceinhand

        #this function rolls the three chosen dies
        def rollthedice (diceinhand):
            # The dice, the color, the result 
            roll1 = diceinhand[0][0] + " " + diceinhand[0][1][random.randint(0,5)]
            roll2 = diceinhand[1][0] + " " + diceinhand[1][1][random.randint(0,5)]
            roll3 = diceinhand[2][0] + " " + diceinhand[2][1][random.randint(0,5)]

            return roll1, roll2, roll3

        #this function evaluates the rolled dice, 
        #prints the results to the user and returns dice to bag if needed
        #it also checks if the user can roll again
        def evaluateRoll (self, labellist, roll1, roll2, roll3, diceinhand):
            def deleteplz (canvas):
                canvas.destroy()
                #reset shotgun and brain labels 
                self.shotgunlabel.config(text = 0)
                self.brainlabel.config(text = 0)

                #delete previous rolls
                self.labellist[0].config(image = "")
                self.labellist[1].config(image = "")
                self.labellist[2].config(image = "")

                #put roll again button for next player 
                self.rollplz = Button(self, text = "CLICK TO ROLL \n THE DICE",\
                   font = "Ariel 20", bg = "#fb4141", command = self.roll)
                self.rollplz.place(x = 85, y = 540)

            global who
            global tempbrain 
            global tempshotgun
            global set

            #display the rolls to the user
            rolls = [roll1, roll2, roll3]
            count = 0
            movement = 0 

            #go through all rolls, print and tally results 
            for roll in rolls:
                
                if (roll == "Green shotgun blast"):
                    tempshotgun += 1 
                    #update label 
                    if count == 0: 
                        self.greenshotgun = PhotoImage(file = "ZD-G-Shotgun.gif")
                        labellist[count].config(image = self.greenshotgun)
                    elif count == 1:
                        self.greenshotgun1 = PhotoImage(file = "ZD-G-Shotgun.gif")
                        labellist[count].config(image = self.greenshotgun1)
                    elif count == 2:
                        self.greenshotgun2 = PhotoImage(file = "ZD-G-Shotgun.gif")
                        labellist[count].config(image = self.greenshotgun2)

                    #update shotgun label 
                    self.shotgunlabel.config(text = tempshotgun)

                elif (roll == "Yellow shotgun blast"):
                    tempshotgun += 1 
                    #show user 
                    if count == 0: 
                        self.yellowshotgun = PhotoImage(file = "ZD-Y-Shotgun.gif")
                        labellist[count].config(image = self.yellowshotgun)
                    elif count ==1:
                        self.yellowshotgun1 = PhotoImage(file = "ZD-Y-Shotgun.gif")
                        labellist[count].config(image = self.yellowshotgun1)
                    elif count == 2:
                        self.yellowshotgun2 = PhotoImage(file = "ZD-Y-Shotgun.gif")
                        labellist[count].config(image = self.yellowshotgun2)


                    #update shotgun label 
                    self.shotgunlabel.config(text = tempshotgun)

                elif (roll == "Red shotgun blast"):
                    tempshotgun += 1 
                    #show user  
                    if count == 0:
                        self.redshotgun = PhotoImage(file = "ZD-R-Shotgun.gif")
                        labellist[count].config(image = self.redshotgun)
                    elif count == 1:
                        self.redshotgun1 = PhotoImage(file = "ZD-R-Shotgun.gif")
                        labellist[count].config(image = self.redshotgun1)
                    elif count == 2:
                        self.redshotgun2 = PhotoImage(file = "ZD-R-Shotgun.gif")
                        labellist[count].config(image = self.redshotgun2)
                        
                    #update shotgun label 
                    self.shotgunlabel.config(text = tempshotgun)

                elif (roll == "Green brains"):
                    tempbrain += 1
                    #show user  
                    if count == 0:
                        self.greenbrain = PhotoImage(file = "ZD-G-Brain.gif")
                        labellist[count].config(image = self.greenbrain)
                    elif count == 1:
                        self.greenbrain1 = PhotoImage(file = "ZD-G-Brain.gif")
                        labellist[count].config(image = self.greenbrain1)
                    elif count == 2:
                        self.greenbrain2 = PhotoImage(file = "ZD-G-Brain.gif")
                        labellist[count].config(image = self.greenbrain2)

                    #update brain label 
                    self.brainlabel.config(text = tempbrain)

                elif (roll == "Yellow brains"):
                    tempbrain += 1
                    #show user 
                    if count == 0:
                        self.yellowbrain = PhotoImage(file = "ZD-Y-Brain.gif")
                        labellist[count].config(image = self.yellowbrain)
                    elif count == 1:
                        self.yellowbrain1 = PhotoImage(file = "ZD-Y-Brain.gif")
                        labellist[count].config(image = self.yellowbrain1)
                    elif count == 2:
                        self.yellowbrain2 = PhotoImage(file = "ZD-Y-Brain.gif")
                        labellist[count].config(image = self.yellowbrain2)

                    #update brain label 
                    self.brainlabel.config(text = tempbrain)

                elif (roll == "Red brains"):
                    tempbrain += 1
                    #show user 
                    if count == 0:
                        self.redbrain = PhotoImage(file = "ZD-R-Brain.gif")
                        labellist[count].config(image = self.redbrain)
                    elif count == 1:
                        self.yellowbrain1 = PhotoImage(file = "ZD-Y-Brain.gif")
                        labellist[count].config(image = self.yellowbrain1)
                    elif count == 2:
                        self.yellowbrain2 = PhotoImage(file = "ZD-Y-Brain.gif")
                        labellist[count].config(image = self.yellowbrain2)

                    #update brain label 
                    self.brainlabel.config(text = tempbrain)

                elif (roll == "Green runner"):
                    #show user results 
                    if count ==0:
                        self.greenrun = PhotoImage(file = "ZD-G-Feet.gif")
                        labellist[count].config(image = self.greenrun)
                    elif count == 1:
                        self.greenrun1 = PhotoImage(file = "ZD-G-Feet.gif")
                        labellist[count].config(image = self.greenrun1)
                    elif count == 2:
                        self.greenrun2 = PhotoImage(file = "ZD-G-Feet.gif")
                        labellist[count].config(image = self.greenrun2)

                    #Put the dice back in the bag 
                    #The roll number corrosponds with the dice number 
                    if count == 0:
                        set.append(diceinhand[0])
                    elif count ==1:
                        set.append(diceinhand[1])
                    elif count == 2: 
                        set.append(diceinhand[2])

                elif (roll == "Yellow runner"):
                    #show user results 
                    if count == 0:
                        self.yellowrun = PhotoImage(file = "ZD-Y-Feet.gif")
                        labellist[count].config(image = self.yellowrun)
                    elif count == 1:
                        self.yellowrun1 = PhotoImage(file = "ZD-Y-Feet.gif")
                        labellist[count].config(image = self.yellowrun1)
                    elif count == 2:
                        self.yellowrun2 = PhotoImage(file = "ZD-Y-Feet.gif")
                        labellist[count].config(image = self.yellowrun2)

                    #Put the dice back in the bag 
                    #The roll number corrosponds with the dice number 
                    if count == 0:
                        set.append(diceinhand[0])
                    elif count ==1:
                        set.append(diceinhand[1])
                    elif count == 2: 
                        set.append(diceinhand[2])

                elif (roll == "Red runner"):
                    #show user results 
                    if count == 0:
                        self.redrun = PhotoImage(file = "ZD-R-feet.gif")
                        labellist[count].config(image = self.redrun)
                    elif count == 1:
                        self.redrun1 = PhotoImage(file = "ZD-R-feet.gif")
                        labellist[count].config(image = self.redrun1)
                    elif count == 2:
                        self.redrun2 = PhotoImage(file = "ZD-R-feet.gif")
                        labellist[count].config(image = self.redrun2)

                    #Put the dice back in the bag 
                    #The roll number corrosponds with the dice number 
                    if count == 0:
                        set.append(diceinhand[0])
                    elif count ==1:
                        set.append(diceinhand[1])
                    elif count == 2: 
                        set.append(diceinhand[2])

                count += 1
            

            #If they die let them know and switch players 
            if tempshotgun >=3:
                killed = True

                #reset temporary rolls and bag of dice 
                tempbrain = 0 
                tempshotgun = 0 
                set = fulldicebag()

                #remove again button 
                self.question.destroy()
                self.again.destroy()
                self.bank.destroy()
                self.rollplz.destroy()


                #show them they have died 
                cann = Canvas(self, width = 410, height = 450)
                cann.config(highlightbackground = "black", \
                    highlightthickness = 3)
                cann.place(x = 500, y = 150)

                #show image on canvas 
                self.shot = PhotoImage(file = "You were shot too many times!.gif")
                self.dead = Label(cann, image = self.shot)
                self.dead.place( x = 5, y = 5)
                print("happening")
                #button to delete 
                self.okay = Button(cann, text ="Okay", font = "ariel 15", \
                    command = lambda: deleteplz(cann))
                self.okay.place(x = 300, y = 410)


                #change the player playing 
                if who == len(names)-1:
                    who = 0
                else: 
                    who += 1

                #change the player playing label 
                self.turn.config(text = str(names[who]) + "'s turn")

            else:
                killed = False

            return killed

        #this function determines if the user wants to go again or not
        def bankoragain(self):
            global who

            #user does not want to go again, save score and switch players 
            def no(self):
                global who 
                global set 
                global tempbrain
                global tempshotgun

                again = False
                winner = False

                #get rid of again buttons 
                self.question.destroy()
                self.again.destroy()
                self.bank.destroy()

                #reset shotgun and brain labels 
                self.shotgunlabel.config(text = 0)
                self.brainlabel.config(text = 0)

                #delete previous rolls
                self.labellist[0].config(image = "")
                self.labellist[1].config(image = "")
                self.labellist[2].config(image = "")


                #add up players score 
                scores[who] += tempbrain
                scorelabels[who].config(text = scores[who])

                #check for a winner 
                for x in range(len(scores)):
                    if (brainstowin <= scores[x]):
                        winner = names[x]
                        winningscore = scores[x]
                        break

                #reset set of dice, brain and shotgun count 
                set = fulldicebag()
                tempbrain = 0
                tempshotgun = 0

                print("the user does not want to go again")

                #always true in this function 
                if not(again):

                    #if there's a winner game over 
                    if winner != False:
                        self.gameover(winner)

                    #if there isn't a winner let the next player play
                    if not(winner):
                       #change the person playing 
                        if who == len(names)-1:
                            who = 0
                        else: 
                            who += 1

                        #change the player playing label 
                        self.turn.config(text = str(names[who]) + "'s turn")

                        #let them invoke roll function again 
                        #put roll button 
                        self.rollplz = Button(self, text = "CLICK TO ROLL \n THE DICE",\
                           font = "Ariel 20", bg = "#fb4141", command = self.roll)
                        self.rollplz.place(x = 85, y = 540)
   
            #Continue by letting user roll again with the same temp scores 
            def yes(self):
                global set 
                global tempbrain 
                global tempshotgun

                #user wants to roll again 
                #choose new dice, roll it, display, evaluate 
                diceinhand = choosedice()
                roll1, roll2, roll3 = rollthedice(diceinhand)
                print(roll1,roll2,roll3)
                killed = evaluateRoll(self,self.labellist,roll1,roll2,roll3,diceinhand)


            #Destroy roll again button 
            self.rollplz.destroy()

            #Show again buttons AND LABEL 
            self.question = Label( self, text = "WOULD YOU LIKE TO ROLL AGAIN?",\
               font = "ariel 20", bg = "#926239")
            self.question.place(x = 360, y = 500)
            self.again = Button(self, text = "Yes, i'll take \n my chances", \
                font= "Ariel 15", bg = "#e792ad", command = lambda: yes(self))
            self.again.place(x = 360, y = 550)
            self.bank = Button(self, text = "No, i'll keep my \n current brains", \
                font = "Ariel 15", bg = "#63c2d6", command = lambda: no(self))
            self.bank.place(x = 560, y = 550)

        #-------------------START OF ROLL FUNCTION ---------------------------
        #global variables 
        global who 
        global tempbrain 
        global tempshotgun 
        global set

        #give them a full set of dice to start
        set = fulldicebag()
        tempbrain = 0 
        tempshotgun = 0

        # chose a dice, roll a dice, evaluate the results 
        diceinhand = choosedice()
        roll1, roll2, roll3 = rollthedice(diceinhand)
        print(roll1,roll2,roll3)
        killed = evaluateRoll(self,self.labellist, roll1,roll2,roll3,diceinhand)

        if not(killed):
            bankoragain(self)
        

    #this occurs when someone has won 
    def gameover(self, winner):
        global brainstowin

        #Make a canvas to declare winner 
        self.win = Canvas(self, width = 1151, height = 756)
        self.win.place(x = 0, y = 0)

        #Background 
        self.winbackground = PhotoImage(file = "Congradulations1.gif")
        self.endbackground = Label(self.win, image = self.winbackground)
        self.endbackground.place(x = 0, y = 0)

        #label with winner name and score 
        self.winneris = Label(self.win, text = winner, font = "ariel 20",\
           bg = "#f8c89f")

        self.winneris.place(x = 570, y = 283)

        #print brains to win 
        self.score2beat = Label(self.win, text = brainstowin, \
            font = "ariel 20", bg = "#f8c89f")

        self.score2beat.place(x = 620, y = 398)

        #quit button 
        self.gamedone = Button(self.win, text = "Press to Exit", \
            font = "ariel 30", command = lambda: quit(), bg = "red")

        self.gamedone.place(x = 765, y = 620)


#Function that initializes the dice back to normal 
def fulldicebag ():

    #make each dice
    red = ['Red',['shotgun blast', 'shotgun blast', 'shotgun blast',\
       'runner', 'runner', 'brains']]

    yellow = ['Yellow',['shotgun blast', 'shotgun blast', 'runner', \
        'runner', 'brains', 'brains']]

    green = ['Green',['shotgun blast', 'runner', 'runner', 'brains', \
        'brains', 'brains']]

    #make bag of dice, shuffle, and return it 
    alldice = [red, red, red, yellow, yellow, yellow, yellow, green,\
       green, green, green, green, green]

    random.shuffle(alldice)
    return alldice


#-------------------------------START OF PROGRAM-----------------------

#Run class to prompt GUI 
app = mainpage()

#loop so window does not close 
app.mainloop()

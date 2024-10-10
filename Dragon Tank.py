#Dragon Tank - Text-based Python Game
#By: Simon Brown
#Dec. 7th - 14th, 2022

from time import sleep #saves having to type all of 'time.sleep()' every time
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from playsound import playsound

#Make sound in game 

######NOT ACC ABOUT DRAGONS!!! Idea::: Plot twist in the end, you're actually like a broken/mentally ill guy I guess, and this whole thing is you preparing to do a mass violence crime, not actually about dragon tanks
        #Instead of the voice in your head being kinda the dragon's will, it'd be like actual voices in your head#

#Print big ascii logo thing



def ellipses(): #Prints 3 dots (ellipses) slowly
    dots = ['','.','.','.']

    for i in dots:
        print(i, end='')
        sys.stdout.flush() #Flushes (clears) data buffer, prints text on the same line
        sleep(0.75)
    print('')
    
def lineBreak():
    dots = ['.','.','.']

    for i in range(25):
        for i in dots:
            print(i, end='')
            sys.stdout.flush()
            sleep(0.009)
    print('')

def typewrite(text, waitTime): #Gives a typewriter effect for displaying text, ie. the letters print one at a time at a high speed
    split = [*text] #Converts text into a List of its characters

    for i in text:
        print(i, end='')
        sys.stdout.flush()
        sleep(0.005) #0.02 in final
    sleep(waitTime)
    print('')

def Tutorial(): #Instructions for player
    typewrite('In Dragon Tank, your goal is to find all the pieces of dragon and assemble them into a kickass tank so you can beat the evil dragons!!',0)
    typewrite("Similar to other games of this nature, you'll be using a command system to move around/do actions in general. Here's how it'll go:",0)
    typewrite("Use keywords from the prompt you're given to do the action. Keywords that you can use to perform actions will be capitalized, for example: 'Pick Up the item'. ",0)
    ellipses()

    action = input("Do you understand the instructions? Y/N\n").lower()
    
    if action == "y":
        typewrite('Off we go then...', 2)
        MainGame()
    elif action == "n":
        print("That's okay, I've got nowhere to be..")
        sleep(1)
        Tutorial()


    

def MainGame(): #Main game segment
    TimeLeft = 48 #0 = game over, depending on what player has done
    typewrite("2 Days Until The End\n", 1)#2 or 3 in final# 
    typewrite('You awaken inside a cave...taking in your dimly lit makeshift bed and few supplies left, painful memories flood in as your last bits of unconsciousness float away. That brief moment of ignorant bliss, gone once more, until tomorrow. Will you Get Up out of bed or Stay and contemplate?\n',0)
    
    #Will follow two different story paths from this point forward (time permitting, I've restarted the story enough times already...)
    choosePath = True
    Dreaming = False #Setup for different endings
    while choosePath == True:
        StoryBed = input()
        match StoryBed:
            case "get up":
                conf = input("Are you sure? It's so warm and cozy... (Y/N)\n").lower()
                if conf == "y":
                    print('Fine then...')
                    ellipses()
                    print('Have it your way.\n')
                    TrueRoute = True #True ending, time permitting
                    choosePath = False
                elif conf == "n":
                    print('So then? Get Up or Stay?') 
                else:
                    print('Get Up or Stay?')


            case "stay" | "stay in bed" : #################################Make more of a bridge between this and "leaving", have actual contemplation
                print("That's right :)")
                ellipses()
                print('Off we go then!')
                BadRoute = True #Bad ending, time permitting
                Dreaming = True
                choosePath = False
                
            case _: #Essentially the 'else' case
                print('Get Up or Stay?\n')
                
        continue   
    
    
    #True Route:

    
    typewrite('So you get out of bed. Better prepare for your journey. Should you wear your armor or not? It can be dangerous out there, but pretty cumbersome to haul around. You might end up going slower... (Y/N)\n', 0)
    chooseArmr = True
    armrMsg = ''
    while chooseArmr == True:
        EqpArmr = input().lower()
        
    
        if EqpArmr == 'y':
            ArmorOn = True #Travelling will take + 5 hours
            chooseArmr = False
            armrMsg = "Armor equipped!"
        elif EqpArmr == "n":
            ArmorOn = False
            chooseArmr = False
            armrMsg = " "
        else:
            print('Y/N?')
        continue
    
        

    typewrite(f'So you venture off! {armrMsg}',0) #Gives message if armor is equipped
    typewrite('Bursting out of the tight entrance of your hidey-hole, you enter...',0)
    ellipses()

    #Printing ascii signage 
    cprint(figlet_format('The Main Cavern', font='big'),
       'white',)

    typewrite("Loading...", 3)

    ###MAIN CAVERN###
    typewrite("You have one goal: Gather the 4 parts, assemble. Time is of the essence! We're all counting on you...",0)
    typewrite(f"{TimeLeft} hours left...",0)

    #Pre-emptive area
    desc1G = True
    compassGet = False
    actionList = ['- Look for dropped items','- Examine the Walls','- Advance']

    while desc1G == True:
        if Dreaming == False:
            desc1Sleep = ("- Go Inside and Sleep :)")
        else:
            desc1Sleep = ''
        
        for i in actionList:
            typewrite(i,0)
            
        sleep(0.5)
        print(desc1Sleep)

        desc1 = input('').lower()
    
        match desc1:
            case "look" | "look for dropped items":
                typewrite("You look on the ground surrounding the dim light coming from your home and find",0)
                ellipses()
                typewrite('A compass!',0)
                compassGet = True 
                actionList.remove(actionList[0]) #Removes unneeded action from option list
                
            case "examine" | "examine the walls":
                typewrite("Stories from the past are etched upon the jagged walls of a cave long abandoned. You see the tales of your ancestors and your brethren, advancing through the ages as you follow along the wall. The pain of being the only one left hurts unlike anything else. You have to do this.",0)
                actionList.remove('- Examine the Walls')
                
            case "go inside" | "sleep":
                print("Just what you need...")
                TimeLeft -= 1 #1 hour to "sleep"...when does it end?
                Dreaming = True

            case "advance":
                if compassGet != True:
                    typewrite("You don't know where to go! Maybe if you had a compass you could keep exploring...",0) #Prevents progress without necessary item
                else:
                    desc1G = False
                
                
            case _:
                typewrite('Look, Examine Walls, or Advance?',0)
                if Dreaming == False: #If bad ending not already going
                    print('or Sleep :)')
        continue

    typewrite(f'{TimeLeft} hours left...',0)    
    typewrite("Advancing onwards, you come to a...double fork in the road? There's 4 different paths to take, you can classify them with your compass: \n- West\n- Northwest\n- Northeast\n- East",0)

    direction = input('').lower()

    def WestPath(): #West Cavern, part 1 of 4
        paper = [] #List to attach writing
        WestActions = ['- Write on the Paper','- Look at the Wall','- Stick your Finger in a Hole']
        typewrite(f"{TimeLeft} hours left...",0)
        typewrite("You walk into the West Cavern and come across an odd looking wall. Are those..holes? You see a piece of paper with a pencil over it and something carved into the wall above it.",0)
        typewrite("What do you do?",0)
        WestWall = True
        

        lookTimes = 1 
        while WestWall == True:
            times = 1
            for i in WestActions:
                typewrite(i,0)

            WestDesc = input('').lower()
            
            
            match WestDesc:
                case "write on the paper" | "write" | "paper":
                    writing = str(input('What do you write?\n'))
                    paper.append(writing)
                    if times == 1:
                        paperStr = ', '.join([str(i) for i in paper]) #Init string for list conversion
                        typewrite(f'The paper now says: {paperStr}',0)
                    else:
                        paperStr = ''.join(map(str,paper)) #Init string for list conversion
                        typewrite(f'The paper now says: {paperStr}',0)

                    if WestDesc == "answer":
                        typewrite
                    times += 1
                        
                case "look at the wall" | "look" | "wall":
                    if lookTimes == 1:
                        typewrite("Holes of different sizes are scattered across the wall...what could've made these?",0)
                    else:
                        typewrite('Nice ass riddle here',0)
                    lookTimes += 1    
                        
                case "stick" | "stick finger" | "finger" | "hole":
                    typewrite("It's a little cold...",0)
                    ellipses()
                    typewrite('What did you think was gonna happen?',0)
                    
                    
            continue
                    
        
    
    def NWPATH():
        typewrite("",0)

    def NEPATH():
        typewrite("",0)

    def EastPath():
        typewrite("",0)

    match direction: 
        case "west":
            typewrite("Travelling West...",0)
            if ArmorOn == True: #Takes longer to travel with heavy armor
                TimeLeft -= 7
                typewrite('This armor is really heavy...you need a break (-2 extra hours)',0)
            else: 
                TimeLeft -= 5
            ellipses()
            WestPath() #Goes down to West Cavern
        case "northwest":
            typewrite("Travelling NW...",0)
            ellipses()
            if ArmorOn == True:
                TimeLeft -= 7
                typewrite('This armor is really heavy...you need a break (-2 extra hours)',0)
            else: 
                TimeLeft -= 5
            NWPath()
        case "northeast":
            typewrite("Travelling NE...",0)
            ellipses()
            if ArmorOn == True:
                TimeLeft -= 7
                typewrite('This armor is really heavy...you need a break (-2 extra hours)',0)
            else: 
                TimeLeft -= 5
            NEPath()
        case "east":
            typewrite("Travelling East...",0)
            ellipses()
            if ArmorOn == True:
                TimeLeft -= 7
                typewrite('This armor is really heavy...you need a break (-2 extra hours)',0)
            else: 
                TimeLeft -= 5
            EastPath()
        
        


     
    
def MainMenu(): #Main menu for starting the game
    
    play = input('Dragon Tank Main Menu:\n1) New game (tutorial)\n2) Skip tutorial\n3) Quit\n').lower()
    match play:
        case "new game" | "1":
            Tutorial()
        case "skip tutorial" | "2":
            MainGame()
        case "quit" | "3":
            quit()
        case _:
            MainMenu()




MainMenu() #Functions aren't called by default

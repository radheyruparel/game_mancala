#
##Author: Radhey Ruparel
#

#Importing all the modules for the program execution  
import sys
import os 
import random #Importing the random module

#Important code for using graphics.py
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def mancala_board_background(graphic_ui):
    '''This funtion prints the static background of the Mancala Such as holes and headings.
    This function as graphic_ui as its paratmeter varible, it is a graphical variable.'''
    
    #This prints the main header of the game 'Mancala' at the centenr on top with big fonts
    graphic_ui.text(350,50,'MANCALA','goldenrod2',50)
    
    #This prints the 'Player 1' heading on the player 1's store
    graphic_ui.text(47,90,'Player 1','black',20)
    #This prints Player 1's store hole
    graphic_ui.rectangle(10,115,75,175,'dark green')
    
    #This loop prints all the holes for player 1
    x_position=111
    NUMBER_OF_SQUARE_P1=5 #Because each player has 5 holes
    while NUMBER_OF_SQUARE_P1>0:
        graphic_ui.rectangle(x_position,215,75,75,'dark green') #A hole of 75 by 75 pixels
        x_position+=100 #Hole should be printed after next 100 pixels, for evenly spacing  
        NUMBER_OF_SQUARE_P1-=1 #To fail the loop
    
    #This prints the 'Player 2' heading on the player 1's store
    graphic_ui.text(651,90,'Player 2','black',20)
    #This prints Player 2's store hole
    graphic_ui.rectangle(615,115,75,175,'dark blue')
    
    #This loop prints all the holes for player 2
    x_position=111
    NUMBER_OF_SQUARE_P2=5 #Because each player has 5 holes
    while NUMBER_OF_SQUARE_P2>0:
        graphic_ui.rectangle(x_position,115,75,75,'dark blue') #A hole of 75 by 75 pixels
        x_position+=100 #Hole should be printed after next 100 pixels, for evenly spacing  
        NUMBER_OF_SQUARE_P2-=1 #To fail the loop

def player_gameplay(pits_chips, store_player_one, store_player_two, player_turns):
    
    '''This function maintains the mathemaical logic of the mancale, manages the values of the holes,
    checking for statifing conditions for store addition. It also decide which players turn it is. 
    This function as pits_chips as a list varaible, this list store all the values of the pits for both the players
    Another paratmeter varable is store_player_one, which is an integer variable, which stores the value of store for player one
    Other paratmeter varable is store_player_two, which is an integer variable, which stores the value of store for player two
    Other paratmeter varable is player_turns, which is an integer variable, this varable determines the chance of the palyer'''

    while player_turns<3: #This loop only fail one of player's turn is over
        while player_turns==1: #This loop is for the input of the frist player
            
            #This takes the player one's input for the selection of the hole
            player_1_selection_pit=int(input('Player 1: Enter position to start moving chips at: '))
            pit_index=player_1_selection_pit-1 #This creates the list index for the pit based on the user input of selection
            chips_in_hole=pits_chips[pit_index] #This copies the value of the value at that index to a int varaible
            pits_chips[pit_index]=0 #This turn at the pit in the list to zero
            
            #This loop is responsable for sowing for player one based on selection
            while chips_in_hole>0: #So if the that selected pit is not zero the we can do the process of sowing
                pit_index+=1 #This take the index of list to next pit for sowing
                pits_chips[pit_index]=pits_chips[pit_index]+1 #Add one to the next pit, till the pit is empty
                chips_in_hole-=1 #To fail the loop when there nothing left in the pit
                if pit_index>8: #If the sowing index get outside the loop 
                    pit_index=-1 #In order for the sowing to move counter-clockwise 
                if chips_in_hole==1 and pits_chips[(pit_index+1)]==0: #Checking if the first conditions for addition of the store matches 
                    chips_in_hole-=1 #Then empty the pit
                    store_player_one+=1 #Add one to the player one's store
                if chips_in_hole==1 and pit_index==-1: #Checking if the second conditions for addition of the store match
                    chips_in_hole-=1 #Then empty the pit
                    store_player_one+=1 #Add one to the player one's store
            player_turns=3 #This fails the main loop for the next player to have the turn will this fucntion is called
            
        while player_turns==2: #This loop is for the input of the second player
            
            #This takes the player one's input for the selection of the hole
            player_2_selection_pit=int(input('Player 2: Enter position to start moving chips at: '))
            pit_index=(player_2_selection_pit-1)+5 #This creates the list index for the pit based on the user input of selection, according to the position of the list
            chips_in_hole=pits_chips[pit_index] #This copies the value of the value at that index to a int varaible
            pits_chips[pit_index]=0 #This turn at the pit in the list to zero
            if pit_index==9:
                    pit_index=-1
            
            #This loop is responsable for sowing for player two based on selection
            while chips_in_hole>0: #So if the that selected pit is not zero the we can do the process of sowing
                if chips_in_hole==1 and pits_chips[(pit_index+1)]==0: #Checking if the first conditions for addition of the store matches
                    chips_in_hole-=1 #Then empty the pit
                    store_player_two+=1 #Add one to the player two's store
                pit_index+=1 #This take the index of list to next pit for sowing
                pits_chips[pit_index]=pits_chips[pit_index]+1 #Add one to the next pit, till the pit is empty
                chips_in_hole-=1 #To fail the loop when there nothing left in the pit
                if pit_index>8: #If the sowing index get outside the loop 
                    pit_index=-1  #In order for the sowing to move counter-clockwise 
                if chips_in_hole==1 and pit_index==5: #Checking if the second conditions for addition of the store match
                    chips_in_hole-=1 #Then empty the pit
                    store_player_two+=1 #Add one to the player one's store
            player_turns=3 #This fails the main loop for the next player to have the turn will this fucntion is called
    return pits_chips,store_player_one,store_player_two #This returns the 





#Declaring the main function
def main():
    
    #This prints out the canvas of 700 by 300 pixles with 
    CANVAS_HEIGHT=300
    CANVAS_WIDTH=700
    gui=graphics(CANVAS_WIDTH,CANVAS_HEIGHT,'MANCALA') 
    
    pits_chips=[3,3,3,3,3,3,3,3,3,3] #This is the list which as all the values of pit
    store_player_one=0 #This int varable store the value of store of player one
    store_player_two=0 #This int varable store the value of store of player two
    
    '''This code outside the loop is just to print a pre-set game board before starting the gameplay, hence the
    store of the both players will be zero. All the holes will have the value of 3'''
    mancala_board_background(gui) #This call the function, to print out the static background of the manacala game board
    gui.text(48,203,str(store_player_one),'white',40) #This prints the store of player one
    #This loop prints the values of pits from the list on the holes for player one
    player_one_index_printing=0  
    pit_printing_x_coord=149
    while player_one_index_printing<5: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 0 to 4
        gui.text(pit_printing_x_coord,253,str(pits_chips[player_one_index_printing]),'white',40) #Text for printing the item from the list on the hole
        pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally 
        player_one_index_printing+=1 #To fail  the loop
    
    #This loop prints the values of pits from the list on the holes for player two
    gui.text(653,203,str(store_player_two),'white',40)
    
    #This loop prints the values of pits from the list on the holes for player two
    player_two_index_printing=9
    pit_printing_x_coord=149
    while player_two_index_printing>4: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 5 to 9, but in decesending order
        gui.text(pit_printing_x_coord,153,str(pits_chips[player_two_index_printing]),'white',40) #Text for printing the item from the list on the hole
        pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally
        player_two_index_printing-=1 #To fail  the loop
    gui.update_frame(20) 
    
    while True: #This an Infintly loop for the game to continue untill one of the player wins
        while True: #This loop control the turns of the player one
            gui.clear() #This clears the frame for the new output to be printed 
            mancala_board_background(gui) #This call the function, to print out the static background of the manacala game board
            #This call the gameplay function for player one
            pits_chips, store_player_one,store_player_two=player_gameplay(pits_chips,store_player_one,store_player_two,1) 
            gui.text(48,203,str(store_player_one),'white',40) #This prints the store of player one
            
            #This loop prints the values of pits from the list on the holes for player one
            player_one_index_printing=0  
            pit_printing_x_coord=149
            while player_one_index_printing<5: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 0 to 4
                gui.text(pit_printing_x_coord,253,str(pits_chips[player_one_index_printing]),'white',40) #Text for printing the item from the list on the hole
                pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally 
                player_one_index_printing+=1 #To fail  the loop
            
            #This loop prints the values of pits from the list on the holes for player two
            gui.text(653,203,str(store_player_two),'white',40)
            
            #This loop prints the values of pits from the list on the holes for player two
            player_two_index_printing=9
            pit_printing_x_coord=149
            while player_two_index_printing>4: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 5 to 9, but in decesending order
                gui.text(pit_printing_x_coord,153,str(pits_chips[player_two_index_printing]),'white',40) #Text for printing the item from the list on the hole
                pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally
                player_two_index_printing-=1 #To fail  the loop
            gui.update_frame(20) #This updates the frame for the next display output 
            
            if store_player_one==3: #If the player one is the first one to get 3 points in the store
                print('Player 1 wins!') #To declare player one won
                any_key_exit=input('Press any key to exit')
                break #To exit the game
            break #To alternate chances 
        
        while True: #This loop control the turns of the player two
            gui.clear() #This clears the frame for the new output to be printed 
            mancala_board_background(gui) #This call the function, to print out the static background of the manacala
            #This call the gameplay function for player two
            pits_chips, store_player_one,store_player_two=player_gameplay(pits_chips,store_player_one,store_player_two,2)
            
            gui.text(48,203,str(store_player_one),'white',40)  #This prints the store of player one
            
            #This loop prints the values of pits from the list on the holes for player one
            player_one_index_printing=0
            pit_printing_x_coord=149
            while player_one_index_printing<5: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 0 to 4
                gui.text(pit_printing_x_coord,253,str(pits_chips[player_one_index_printing]),'white',40) #Text for printing the item from the list on the hole
                pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally 
                player_one_index_printing+=1 #To fail  the loop
                
            #This loop prints the values of pits from the list on the holes for player two
            gui.text(653,203,str(store_player_two),'white',40)
            
            #This loop prints the values of pits from the list on the holes for player two
            player_two_index_printing=9
            pit_printing_x_coord=149
            while player_two_index_printing>4: #As we have 5 holes, it will print one item from the list to one hole, hence for player it will print from list index 5 to 9, but in decesending order
                gui.text(pit_printing_x_coord,153,str(pits_chips[player_two_index_printing]),'white',40) #Text for printing the item from the list on the hole
                pit_printing_x_coord+=100 #Next text should be printed after 100 pixels horizontally
                player_two_index_printing-=1 #To fail  the loop
            gui.update_frame(20) #This updates the frame for the next display output 
            
            
            if store_player_two==3: #If the player one is the first one to get 3 points in the store
                print('Player 2 wins!') #To declare player two won
                any_key_exit=input('Press any key to exit')
                break #To exit the game
            break  #To alternate chances 
    pass

#Calling the main function
main()

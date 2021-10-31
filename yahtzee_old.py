#############################################################
# Program Name: Final Exam Project (yahtzee.py)             #
#							    #
# Date: 2020-11-23                                          #
#							    #
# Descrption: Yahtzee main program with a menu and GamePlay #
# The program uses two classes Roll to implement dice rolls #
# and a Player class to store and display scores            #
#                                                           #
# Additional project files roll.py, player.py          	    #
# Execution: Run Module(F5) for yahtzee.py                  #
#                                                           #
# Author: Maori Brown           			    #
#############################################################

#import random
from player import Player
from roll import Roll



#############################################################
# Funtion Name: mainMenu                                    #
# Descrption: Menu displays rules and intiates game play    #
#############################################################

def yahtzeeMenu():

     # while loop used to control rules viewing and game launch
     while True:
      Menu = input("Welcome to Yahtzee!\n\nPress R for the rules of the game:")

      if Menu == ("R") or Menu ==("r"):
        rules = input("\n\n\t\t\t\tObjective\n\nIn this Yahtzee game you can roll 5 dice first for the top score and then the bottom score.\
          \nA player gets 3 rolls and can hold any of the dice.\
          \nA player can score on any roll\n . \
          \n\nThe game ends when one of the following occurs: . \
          \n\n 1. Once all scoring options are used.\
          \n\n 2. The player ends the game and is prompted to save it..\
          \n\n\t\t\t\tScoring\n.\
          \nfor the upper scoring a bonus of 35 is awareded for any score over 63 .\
          \nSmall straights score 30 and a large 40 points.\n\nYahtzee is 5 of a kind and scores 50 points, second Yahtzee is bonus 50 points \
          \n\n\t\t\t\t How to Play\n\nIn order to keep dice, you must enter the number that you are wanting to keep that is displayed.\
          \n\ni.e. If you rolled (5,2,4,1,5) and you wanted to keep the 2,4, and 1, you must enter \"2,4,1\"\n\nWould you like to start now? (Y/N):")
        
        if rules == ("Y") or rules == ("y"):
            print("\n"*5)
            break
        elif rules == ("N") or rules == ("n"):
            print("Back to Yahtzee Menu\n")
        else:
            print("\n"*5)
            rules="Y"
            break

#############################################################
# Funtion Name: gamePlay                                    #
# Descrption: controls the running of the game              #
#############################################################

def gamePlay():
  
    '''
    method holding the game play for our Yahtzee game.
    '''

    #Creating the dictionaries, and roll and player objects
    
    #defining what we work with on the top part of the game.
    game_list_top = ['aces' , 'twos' , 'threes' , 'fours' , 'fives' , 'sixes']
    game_list_top_values = [1,2,3,4,5,6]

    #defining what we work with on the bottom part of the game.
    game_list_bottom = ['threeOfAKind' , 'fourOfAKind' , 'fullHouse','smallStraight','largegStraight','Yahtzee','Chance','Yahtzee2']
    game_list_bottom_values = [1,2,3,4,5,6,7,8]

    
    #create a player and a dice to play.
    player1 = Player('Maori')
    dice1 = Roll()

    # Run topScore to get top scorecard
    topScore(game_list_top,game_list_top_values,player1,dice1)
    
    # Run topScore to get bottom scorecard
    bottomScore(game_list_bottom,game_list_bottom_values,player1,dice1)

    #print total Scores
    totalScore = player1.get_top_score()
    totalScore = totalScore + player1.get_bottom_score()
    print ('-'*40)
    print (f'TotalScore:  {totalScore}')
    print ('-'*40)

    save = input("Do you want to quit and save the game? (Y/N)")
    if save == ("Y") or save ==("y"):
         print("Goodbye\n")
         print ('-'*40)
         print (f'TotalScore:  {totalScore}')
         print ('-'*40)
         player1.save_scoreboard()
    elif save == ("N") or save ==("n"):
         gamePlay()
         
    

#############################################################
# Funtion Name: topScore                                    #
# Descrption: controls the running of Yahtzee top scoring   #
#############################################################

def topScore(game_list_top,game_list_top_values,player1,dice1):
    '''
    method holding the topScore for our Yahtzee game.
    '''
    
    #loop through the top part and start rolling some dice!
    for index,item in enumerate(game_list_top):

        #just one way to print info on the current rolling
        print ('-'*40)
        print (f'rolling for {item}')
        print ('-'*40)

        #first roll:
        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        #second roll:
        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        #third roll:
        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        #the final roll collection of dice goes in for check:
        final_roll_collection = dice1.get_kept_dice()

        print (f'final roll collection: {final_roll_collection}')

        #check what the score is for this particular roll:
        check_score = dice1.single_values(final_roll_collection,game_list_top_values[index])

        #create the key in the dictionary and add the score to the total top score.
        #this score will later determine if we get a bonus or not.
        player1.add_rolled(item , check_score)
        player1.add_top_score(check_score)

    #let's hope we get a bonus?
    player1.add_top_bonus()

    #just one way to print info on the current rolling
    print ('-'*40)
    print ("Top Scores")
    print ('-'*40)
        
    #print current score:
    player1.print_scoreboard()
    print ('-'*40)


#############################################################
# Funtion Name: bottomScore                                 #
# Descrption: controls the running of Yahtzee bottomScoring #
#############################################################

def bottomScore(game_list_bottom,game_list_bottom_values,player1,dice1):
    '''
    method holding the game play for our Yahtzee game.
    '''

    #just one way to print info on the current rolling
    print ('-'*40)
    print ("Bottom Scores")
    print ('-'*40)
    
    #loop through the bottom part and start rolling some dice!
    for index,item in enumerate(game_list_bottom):

        #just one way to print info on the current rolling
        print ('-'*40)
        print (f'rolling for {item}')
        print ('-'*40)

        #first roll:
        dice1.roll_dice()
        keep1 = dice1.keep_dice()

        #second roll:
        dice1.reroll_dice(keep1)
        keep2 = dice1.keep_dice()

        #third roll:
        roll3 = dice1.reroll_dice(keep2)
        dice1.forced_keep(roll3)

        #the final roll collection of dice goes in for check:
        final_roll_collection = dice1.get_kept_dice()

        print (f'final roll collection: {final_roll_collection}')

        #create the key in the dictionary and add the score to the total bottom score.
        #check what the score is for each particular roll:
        
        if game_list_bottom[index] == 'threeOfAKind':
             check_score = dice1.check_three_kind(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Three of a Kind Score: ",check_score)
             
        if game_list_bottom[index] == 'fourOfAKind':
             check_score = dice1.check_four_kind(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Four of a Kind Score: ",check_score)

        if game_list_bottom[index] == 'fullHouse':
             check_score = dice1.check_full_house(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Full House Score: ",check_score)

        if game_list_bottom[index] == 'smallStraight':
             check_score = dice1.check_small_straight(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Small Straight Score: ",check_score)

        if game_list_bottom[index] == 'largegStraight':
             check_score = dice1.check_large_straight(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Large Straight Score: ",check_score)
          
        if game_list_bottom[index] == 'Yahtzee':
             check_score = dice1.check_yahtzee(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Yahtzee!!!!: ",check_score)

        if game_list_bottom[index] == 'Chance':
             check_score = dice1.add_chance(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Chance Score: ",check_score)
             print ('-'*40)

        if game_list_bottom[index] == 'Yahtzee2':
             check_score = dice1.check_yahtzee2(final_roll_collection)
             player1.add_rolled(item , check_score)
             player1.add_bottom_score(check_score)
             print("Yahtzee Bonus!!!!: ",check_score)    

    
    
        
    #print current score:
    player1.print_scoreboard()    

#############################################################
# Funtion Name: yahtzee                                     #
# Descrption: controls menu and game play functions         #
#############################################################

def yahtzee():
     # Displays the Menu and launches game play    
     yahtzeeMenu()

     # gamePlay is launched once player exits the menu 
     gamePlay()

#Launch the Game
yahtzee()     

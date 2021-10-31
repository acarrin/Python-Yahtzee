#############################################################
# Program Name: Final Exam Project (roll.py)                #
#							    #
# Date: 2020-11-23                                          #
#							    #
# Descrption: Yahtzee roll class to provide roll            #
# functionality for game play                               #
#                                                           #
# Execution: object instantiated by yahtzee module run	    #
#                                                           #
# Author: Andrew Carrington           			    #
#############################################################
import random
from cImage import *

class Roll:
    def __init__(self):
        '''
        class holding all the dice functionality for rolling the dice, but
        also checking dice values for the gameplay
        '''
        self._current_dice_list = []
        self._current_kept_dice = []
        self._current_image_list = []
        self._current_offset = 0
        

    #this section focuses on the rolling of dice logic.

    def roll_dice(self):
        '''
        method function returning a dice list with random values between 1 to 6
        like a die would function in real life.
        - returns list
        '''
        self._current_kept_dice.clear()
        self._current_dice_list = [random.randint(1,6) for die in range(0,5)]
        print (f'you rolled {self._current_dice_list} ! \n')

        return self._current_dice_list

 
    def keep_dice(self):
        '''
        method function returning a dice list to reroll.
        It also stores the dice you want to keep in a separate keep list.
        - returns list
        '''
        
        keep_input = input('which dice do you want to keep (comma separated: e.g. 1,1,5)? ')
        split_input = keep_input.split(',')

        if keep_input == '':
            return self._current_dice_list
        
        for die in split_input:
            if not die.isdigit():
                print (f'please try again, integer is required as input')
                keep_input = input('which dice do you want to keep (comma separated: e.g. 1,1,5)? ')
                split_input = keep_input.split(',')
                #split_input_int = [int(item) for item in split_input]

        split_input_int = [int(item) for item in split_input]
        

        for die in split_input_int:
            self._current_kept_dice.append(die)

        #cycle through list user wants to keep
        for value in split_input_int:
            if value in self._current_dice_list:
                self._current_dice_list.remove(value)

        return self._current_dice_list


    def reroll_dice(self, dice_list):
        '''
        method function returning current dice list just like the initial roll.
        This time it uses the returned list after the player keeps some dice.
        (This could probably be refactored into roll so roll and reroll are the same,
        but with different arguements.)
        '''
        self._current_dice_list = [random.randint(1,6) for die in range(0,(len(dice_list)))]
        print (f'You rolled {self._current_dice_list} ! \n')
        return self._current_dice_list

    def get_current_dice(self):
        '''
        method function returning the current dice list.
        - returns list
        '''
        return self._current_dice_list

    def get_kept_dice(self):
        '''
        method function returning the current kept dice list.
        - returns list
        '''
        return self._current_kept_dice

    def forced_keep(self,dice_list):
        '''
        method used to force the third roll into the keep dice list.
        '''
        for die in dice_list:
            self._current_kept_dice.append(die)


    #this section focuses on the checkup of dice values.

    def single_values(self,dice_list,check_value):
        '''
        method function returning the roll score based on single value checks.
        This is for the top part of the game where you roll aces, twos etc.
        - returns int
        '''
        roll_score = 0
        for die in dice_list:
            if die == check_value:
                roll_score +=die
        return roll_score
        
    def check_three_kind(self, dice_list):
        '''
        function checks if there are at least three identical dice in the dice list.
        - updates scores
        - returns bool
        '''
        dice_list.sort()
        if dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
            roll_score = 0
            for die in dice_list:
                roll_score +=die
            return roll_score
        return False

    def check_four_kind(self, dice_list):
        '''
        function checks if there are at least four equal dice in the dice list.
        - updates scores
        - returns bool
        '''
        dice_list.sort()
        if dice_list[0] == dice_list[3] or dice_list[1] == dice_list[4]:
            roll_score = 0
            for die in dice_list:
                roll_score +=die
            return roll_score
        return False

    def check_full_house(self,dice_list):
        '''
        function checks if the dice are two equal plus three equal in the dice list.
        - updates scores
        - returns bool
        '''
         #sorting the list makes it easier to check items against each other.
        dice_list.sort()

        #if the set representation of the list is 2, we have a possible full house.
        if (len(set(dice_list))) != 2:
            return False

        #to differentiate it from four of a kind, we have to check this:
        elif dice_list[0] != dice_list[1] or dice_list[0] != dice_list[4]:
            return 25
        return False
    
    def check_small_straight(self, dice_list):
        '''
        function checks if the dice in the dice list are in sequence 1-5.
        - updates scoress
        - returns bool
        '''
        #sorting the list makes it easier to check items against each other.
        dice_list.sort()
        if len(set(dice_list)) == 4 and int(dice_list[0]) <= 3:
            return 30

        return False

    def check_large_straight(self, dice_list):
        '''
        function checks if the dice in the dice list are in sequence 2-6.
        - updates scores
        - returns bool
        '''
        dice_list.sort()
        if len(set(dice_list)) == 5 and int(dice_list[1]) == int(dice_list[0]) + 1 and int(dice_list[2]) == int(dice_list[1]) + 1  and int(dice_list[3]) == int(dice_list[2]) + 1 and int(dice_list[4]) == int(dice_list[3] + 1):
            print(dice_list)
            return 40

        return False

    
    def check_yahtzee(self, dice_list):
        '''
        function checks if all the dice in the dice list are equal
        - updates scores
        - returns bool
        '''
        if len(set(dice_list)) == 1:
            return 50
        return False

    def check_yahtzee2(self, dice_list):
        '''
        function checks if all the dice in the dice list are equal
        - updates scores
        - returns bool
        '''
        if len(set(dice_list)) == 1:
            return 50
        return False

    def add_chance(self, dice_list):
        '''
        function does not check anything, just updates score with sum of the dice list
        - updates scores
        - returns bool
        '''
        roll_score = 0
        for die in dice_list:
            roll_score +=die
        return roll_score
        return False

    def get_image(self,dieRoll,oldImg,w,h):
            
        diceWidth = int(w / 6)
        offset = 0

        # Set up the empty image to build the temporary images
        newImg = EmptyImage(w, h)
    
        # Get Offset, print statements were used for debugging
        if dieRoll == 1:
            offset = diceWidth * 0
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
        elif dieRoll == 2:
            offset = diceWidth * 1 + 1
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
        elif dieRoll == 3:
            offset = diceWidth * 2 + 1
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
        elif dieRoll == 4:
            offset = diceWidth * 3 + 1
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
        elif dieRoll == 5:
            offset = diceWidth * 4 + 1
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
        elif dieRoll == 6:
            offset = diceWidth * 5 + 1
            #print("dieRoll: ",dieRoll)
            #print("offset: ",offset)
            
                   
        # set up global offset in case we need it later
        self._current_offset = offset
        #print("Global Offset: ",self._current_offset)
        
        for row in range(h):
            for col in range(diceWidth):
                oldPixel = oldImg.getPixel(col + offset, row)
                newPixel = oldPixel
                newImg.setPixel(col, row, newPixel)
        
        newImg.setPosition(offset, 0)
        #newImg.draw(myImageWindow)
        return newImg    

    def drawDice(self,dice_list):

        imageFile = "dice.gif"
        oldImage = FileImage(imageFile)
        width = oldImage.getWidth()
        height = oldImage.getHeight()
        dWidth = int(width / 6)
        displayOffset = 0        
        dieRollNo = 6
        noOfDice = 5
        
        # Set up the image window
        myImageWindow = ImageWin("Final Dice Roll", int(width/6) * 5, height)

        # Set up a list of empty images
        self._current_image_list = [EmptyImage(width, height) for die in range(0,(len(dice_list)))]

        # Set up a temporary image to display in the image window from the list of images
        img = EmptyImage(width, height)

        # Print statements were used for debugging
        dice_list.sort()
        for j in range(0,5):
            if j == 1:
                displayOffset = dWidth + 1
            elif j > 1:
                displayOffset = dWidth * j + 1
            #print("Value of j: ",j)
            #print("Dice List: ",dice_list)
            #print("Display Offset: ",displayOffset)
            #print("dWidth: ",dWidth)
            self._current_image_list[j] = self.get_image(int(dice_list[j]),oldImage,width,height)
            img = self._current_image_list[j]
            img.setPosition(displayOffset, 0)
            img.draw(myImageWindow)
        myImageWindow.exitOnClick()


    

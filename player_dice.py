#############################################################
# Program Name: Final Exam Project (player.py)              #
#							    #
# Date: 2020-11-23                                          #
#							    #
# Descrption: Yahtzee Player class to provide Player Scores #
# functionality for game play                               #
#                                                           #
# Execution: object instantiated by yahtzee module run	    #
#                                                           #
# Author: Andrew Carrington           			    #
#############################################################

class Player:
    def __init__(self, name):
        '''
        method holding all player data like name and all the scores.
        '''
        self._name = name
        self._scoreboard = {}

        self._top_score = 0
        self._bottom_score = 0
        self._bonus_bottom = 0
        self._total_score = 0
        self._save_file = name + ".txt"

    def add_rolled(self, rolled_type , value):
        '''
        method adding scores to the player scoreboard
        '''
        self._scoreboard[rolled_type] = value

    def add_top_score(self,value):
        '''
        method adding a rolled score to the top part score.
        '''
        self._top_score += value

    def add_bottom_score(self,value):
        '''
        method adding a rolled score to the bottom part score.
        '''
        self._bottom_score += value    

    def add_top_bonus(self):
        '''
        method that checks for top part score. If it is high enough, a bonus
        is added to the scoreboard.
        '''

        #keep this a variable for easy updates.
        needed_score_for_top_bonus = 63

        if self.get_top_score() >= needed_score_for_top_bonus:
            self._scoreboard['top_bonus'] = 35
        else:
            self._scoreboard['top_bonus'] = 0

        self._top_bonus = self._scoreboard['top_bonus']

    def get_top_score(self):
        '''
        method function returning current top part score
        '''
        return self._top_score
    
    def get_bottom_score(self):
        '''
        method function returning current top part score
        '''
        return self._bottom_score

    def print_scoreboard(self):
        '''
        method printing all the values in the scoreboard.
        '''
        for key, value in self._scoreboard.items():
            print (f'{key} : {value}')


    def save_scoreboard(self):
        outFile = open(self._save_file,"w")
        '''
        method saving all the values in the scoreboard.
        '''
        fHeading = "Player Roll"
        cHeading = "Player Score"
        tempHeadings = outFile.write(fHeading.center(10) + " " + cHeading.center(10) + "\n")
        for key, value in self._scoreboard.items():
            outFile.write(f'{key} : {value}' + "\n")
            

        outFile.close()



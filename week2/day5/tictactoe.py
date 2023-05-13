#  9 conditions for each player - as per grid box --


    
# Function for display board 
# Store players input onto the display board
# Create a condition which satifies creation of list 
# if the list contains a row with "x" or "o", player wins

#           Player input condition draft 
#           Condition should state which player is the winner

# 3 lists
# if 'x' or 'o' == list1[0] == list1[§1] == list2[2] 
#               or
# list1[0] == list2[1] == list3[2]
#               or
# list1[3] == list2[1] == list3[0]
#               or
# list1[0] == list2[0] == list3[0]
#               or
# # list1[1] == list2[1] == list3[1]
                # or
# list1[2] == list2[2] == list3[2]
#               or
# list1[3] == list2[3] == list3[3]

# Create nav letters on the left i.e (game_board [DISPLAY])
# Column numbers
# Row letters

#       1      2        3
# A

# B

# C

# Players will select position using navigation characters

# Loop 3 times each for player

# display board - player input display on board
# every input should append a character to the selected 
# position using index : 

# conditionals player_input(): 
# if player x --> odd == 1
# if player 0 --> even == 0

# player - check used position 
# lock position within the board range (maxlen)
# After each move display board 
# manually add the GUI on the code



game_board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

for row in game_board:
    print(row[0] + "  | " + row[1] + " | ")
    print(row[0] + "*"*8)




    

    

# for col in game_board:
#     print(" | ")



























# from random import random 
# from time import time 


# game_board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# print(game_board)

# def display_board():
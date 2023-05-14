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



# game_board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# for row in game_board:
#     print(row[0] + "  | " + row[1] + " | ")
#     print(row[0] + "*"*8)

# for col in game_board:
#     print(" | ")

board = [' ' for _ in range(9)]
current_player = 'X'

def display_board():
    print('-'*13)
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |')
        print('-'*13)


def player_input(player):
    while True:
        position = input(f"player {player}, choose a position (1-9): ")
        if position.isdigit():
            position = int(position)
            if 1 <= position <= 9 and board[position-1] == ' ':
                return position - 1
            print("invalid posiion. Try again.")

def check_win():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return board[combination[0]]
        return None
    
def play():
    global current_player

    while True:
        display_board()
        position = player_input(current_player)
        board[position] = current_player

        winner = check_win()
        if winner:
            display_board()
            print(f"Player {winner} wins!")
            break
        
        if ' ' not in board:
            display_board()
            print("It's a tie!")
            break

        current_player = '0' if current_player == 'X' else 'X'

play()





















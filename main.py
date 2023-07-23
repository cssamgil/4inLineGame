#------global variable----
# 4 in lane
# board game
board = [
         '_','_','_','_',
         '_','_','_','_',
         '_','_','_','_',
         '_','_','_','_',]

# if game is still going
game_still_going = True

winner = None

# Tells us who the current player is (X goes first)
current_player = "X"


# ------------- Functions ---------------
def play_game():

    # display initial boards
    display_board()

    while game_still_going:

        #handle a single turn
        handle_turn(current_player)

        # check if game has ended
        check_if_game_over()

        # flip to other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")


# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] +
          "     01 | 02 | 03 | 04")
    print(board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] +
          "     05 | 06 | 07 | 08")
    print(board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11] +
          "     09 | 10 | 11 | 12")
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] +
          "     13 | 14 | 15 | 16")
    print("\n")


def handle_turn(player):
    print("Welcome to the tic tac toe game!")
    
    
    print(player + "'s turn.")
    position = input("enter a number from  1-16:")
    valid = False
    while not valid:

        while position not in [
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                "13", "14", "15", "16"
        ]:
            position = input('not valid , please choose from 1-16:')

        position = int(position) - 1

        if board[position] == '_':
            valid = True
        else:
            print("you can't go there! go again.")

    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    #get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] == board[3] != '_'
    row_2 = board[4] == board[5] == board[6] == board[7] != '_'
    row_3 = board[8] == board[9] == board[10] == board[11] != '_'
    row_4 = board[12] == board[13] == board[14] == board[15] != '_'

    if row_1 or row_2 or row_3 or row_4:
        game_still_going = False
        #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[4]
    elif row_3:
        return board[8]
    elif row_4:
        return board[12]
    return None


def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] == board[9] != '_'
    column_2 = board[1] == board[4] == board[7] == board[10] != '_'
    column_3 = board[2] == board[5] == board[8] == board[11] != '_'
    column_4 = board[12] == board[13] == board[14] == board[15] != '_'


    if column_1 or column_2 or column_3 or column_4:
        game_still_going = False
        #return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    elif column_4:
        return board[12]
    return None


def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] == board[11] != '_'
    diagonals_2 = board[2] == board[4] == board[6] == board[10] != '_'

    if diagonals_1 or diagonals_2:
        game_still_going = False
        #return the winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return None


def check_if_tie():
    global game_still_going
    if '_' not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# ------------ Start Execution -------------
# Play a game of 4 in line
play_game()

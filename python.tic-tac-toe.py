#----global variables ---

# Game board

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",] 
          
# if game still going
game_still_going = True


#who won? or tie?
winner = None

# whos turn is it
current_player = "X"


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():

  #Display initial board
  display_board()
  # while the game is still going
  while game_still_going:
    # handle a single turn of an arbitrary player
    handle_turn(current_player)
    # check if the game has ended
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended 
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")



# Handle a single turn of an arbitrary player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4","5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

 


    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You cant go there. Go again.")



  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  #set up global variables
  global winner
  #check row
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagnols
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  # Set up global variables 
  global game_still_going
  # check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # retuen the winner ( X or O)  
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  # Set up global variables 
  global game_still_going
  # check if any of the rows have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # retuen the winner ( X or O)  
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
    # Set up global variables 
  global game_still_going
  # check if any of the rows have all the same value (and is not empty)
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
 # if any diagonals does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  # retuen the winner ( X or O)  
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return



def flip_player():
  # global variables we need
  global current_player
  # if the current player was x, then change it to o
  if current_player == "X":
    current_player = "O"
    # if the current player was o, change it to x
  elif current_player == "O":
    current_player = "X"
  return

play_game() 


# board
# display board
# play game
# handle turn 
# check win 
  # check rows
  # check columns 
  # check diagonal 
# check tie 
# flip player 
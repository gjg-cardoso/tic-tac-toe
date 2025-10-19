import os
import random

def clear_screen():
    # Clear screen for better display of the game board
    os.system('cls' if os.name == 'nt' else 'clear')

def new_round():

    '''Returns true if Y for playing another round'''

    answer = ''

    # Receive Y/N
    while answer not in {'Y','N'}:
        answer = input('One more round? (Y/N)').upper()
        if answer not in {'Y','N'}:
            print('Invalid input!')

    return answer == 'Y'

def choose_player():

    '''Radomly decides which player will start'''

    return random.randint(0,1)

def  display_board(board):
    
    '''Display the Tic Tac Toe board in a formatted way.'''

    # Enumerate each site for user input
    site_numbers = [["1.", "2.", "3."],
                    ["4.", "5.", "6."],
                    ["7.", "8.", "9."]]

    # Print the board with site numbers on top
    clear_screen()
    for r, board_row in enumerate(board):
        print('{0:7} | {1:7} | {2:7}'.format(site_numbers[r][0],site_numbers[r][1],site_numbers[r][2]))
        print('{0:^7} | {1:^7} | {2:^7}'.format(*board_row))
        print('{0:^7} | {1:^7} | {2:^7}'.format(*[" ", " ", " "]))
        if r < len(board) - 1:
            print("-" * 27)

# Example usage
#display_board([[" ","O"," "],["X"," "," "],[" "," ","X"]])

def choose_markers(markers):
    '''Choose markers for player 1 and player 2.'''
    
    # Ensure valid input
    while True:
        player1 = input('Player 1, choose your marker ({0} or {1}): '.format(*markers)).upper()
        if player1 in markers:
            markers.remove(player1)
            player2 = markers[0]
            clear_screen()
            break
        else:
            print(f"Invalid choice. Please choose either {markers[0]} or {markers[1]}.")
    return player1, player2

# Example usage
#player1, player2 = choose_markers(["X", "O"])
#print(f"Player 1: {player1}, Player 2: {player2}")

def move_input(board,player):

    '''Receives and checks input from the player'''

    # List available moves
    flatboard = [cell for row in board for cell in row]
    moves = [str(i+1) for i, space in enumerate(flatboard) if space == ' ']

    # Receive and validade input
    player_move = 'wrong input'

    while player_move not in moves:
        player_move = input(f'Player '+str(player+1)+', chose a space (1-9): ')

        if player_move.isdigit() == False or int(player_move) < 1 or int(player_move) > 9:
            print('Invalid input!')
        elif player_move not in moves:
            print('This space is already taken!')
    
    clear_screen()
    return player_move

# Example
#move_input([[" ","O"," "],["X"," "," "],[" "," ","X"]],1)

def update_board(board,move,marker):
    
    '''Updates the board with marker at position specified by the move'''

    board[(int(move)-1) // 3][(int(move)-1) % 3] = marker
    
    return board

# Example
#update_board([[" ","O"," "],["X"," "," "],[" "," ","X"]],"9","G")

def lines(board):
    
    '''Returns all the rows, columns, and diagonals in a single list'''

    columns = [list(col) for col in zip(*board)]
    diagonals = [[board[0][0],board[1][1],board[2][2]],[board[0][-1],board[1][-2],board[2][-3]]]

    all_lines = board + columns + diagonals

    return all_lines

# Example
#lines([["X","O"," "],[" ","X","X"],[" "," ","X"]])

def winning_check(board,marker):

    '''Check if the player with a certain marker won'''

    winning_condition = [marker,marker,marker]

    all_lines = lines(board)

    if winning_condition in all_lines:
        return True
    else:
        return False

# Example
#winning_check([["X","O"," "],[" "," ","X"],[" "," ","X"]],"X")

def draw_check(board,markers):

    '''Check if it is already not possible to win: all lines have both markers'''

    markerset = set(markers)

    for line in lines(board):
        if markerset <= set(line):
            pass
        else:
            return False
    
    return True

# Example
#draw_check([["X","O","X"],[" ","O","X"],["O","X","O"]],["O","X"])

def tic_tac_toe():
    '''Main function to run the Tic Tac Toe game.'''

    print("Welcome to Tic Tac Toe!")

    # Choose the players' markers
    markers = choose_markers(["X", "O"])
    print(f"Player 1 is "+markers[0]+" and Player 2 is "+markers[1]+".")
    wins = [0,0]

    # Loop for multiple rounds
    while True:
    
        # Initialize and display the initial board
        board = [[" " for n in range(3)] for row in range(3)]
        display_board(board)

        # Game loop
        player_turn = choose_player()
        print('Player '+str(player_turn + 1)+' goes first.')

        while True:
            # Player's turn
            new_move = move_input(board,player_turn)
            board = update_board(board,new_move,markers[player_turn])
            display_board(board)

            # Check if the current player won
            if winning_check(board,markers[player_turn]):
                print(f'Player '+str(player_turn + 1)+' wins!')
                wins[player_turn] += 1
                break
        
            # Check for a draw
            elif draw_check(board,markers):
                print("It's a draw!")
                break

            # Move to the next player
            player_turn = (player_turn + 1) % 2

        # Ask for another round
        if new_round() == False:
            break

    print('Player 1 won '+str(wins[0])+' times and Player 2 won '+str(wins[1])+' times!')

if __name__ == "__main__":
    tic_tac_toe()
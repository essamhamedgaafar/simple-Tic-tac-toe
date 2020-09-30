import random
board = ["-","-","-","-","-","-","-","-","-"]
game_on = True
winner = None
def play_game():
    display_board()
    while game_on:
        my_turn()
        check_for_winner()
        pc_turn()
        check_for_winner()
        display_board()
    print(f"winner is : {winner}")

#to display boardcls
def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

#my turn function
def my_turn():
    global board
    while True:
        while True:
            my_choice = input("Enter your choice from 1 to 9 : ")
            try:
                my_choice = int(my_choice)
            except ValueError:
                print("Enter Valid Number Pls")
                continue
            if 0 < my_choice <= 9:
                break
            else:
                print("Enter Value in Range 1 - 9")
                
        my_choice = int(my_choice) - 1
        if board[my_choice] == "-":
            board[my_choice] = "x"
            break
        else:
            print(f"{my_choice + 1} is taken")

#pc Turn Function

def pc_turn():
    global board
    while True:    
        pc_choice = random.randrange(0,9)
        if board[pc_choice] == "-":
            board[pc_choice] = 'o'
            break

# function for checking for a winner
def check_for_winner():
    check_for_win()

def check_for_win():
    global board
    global game_on
    global winner 
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 :
        winner = board[0]
        game_on = False
    elif row2 :
        winner = board[3]
        game_on = False
    elif row3:
        winner = board[6]
        game_on = False
    else:
        pass
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 :
        winner = board[0]
        game_on = False
    elif column2 :
        winner = board[1]
        game_on = False
    elif column3:
        winner = board[2]
        game_on = False
    else:
        pass
    del1 = board[0] == board[4] == board[8] != "-"
    del2 = board[3] == board[4] == board[6] != "-"

    if del1 :
        winner = board[0]
        game_on = False
    elif del2 :
        winner = board[3]
        game_on = False
    else:
        pass

play_game() 
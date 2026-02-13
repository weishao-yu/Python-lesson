row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
counter = 0
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
def user_choice():
    choice = input("Please input number(1 - 9) ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("choice is not vaild")
        else:
            print("not in the range")
        choice = input("Please input number(1 - 9) ")      
    return int(choice)  
def get_counter():
    global counter
    list_symbol = ["X", "O"]
    counter += 1
    return list_symbol[counter % 2]
def update_table(index):
    if index in range(1, 4):
        if row1[index - 1] == ' ':
            row1[index - 1] = get_counter()
            return True
        else:
            return False
    if index in range(4, 7):
        if row2[index - 4] == ' ':
            row2[index - 4] = get_counter()
            return True
        else:
            return False
    if index in range(7, 10):
        if row3[index - 7] == ' ':
            row3[index - 7] = get_counter()
            return True
        else:
            return False
def gamechecking():
    player_1_win = False
    player_2_win = False
    if (row1[0] == row1[1]) and (row1[1] == row1[2]) and (" " not in row1):
        if row1[0] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row2[0] == row2[1]) and (row2[1] == row2[2]) and (" " not in row2):
        if row2[0] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row3[0] == row3[1]) and (row3[1] == row3[2]) and (" " not in row3):
        if row3[0] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row1[0] == row2[0]) and (row2[0] == row3[0]) and ((row1[0] != " ") and (row2[0] != " ") and (row3[0] != " ")):
        if row1[0] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row1[1] == row2[1]) and (row2[1] == row3[1]) and ((row1[1] != " ") and (row2[1] != " ") and (row3[1] != " ")):
        if row1[1] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row1[2] == row2[2]) and (row2[2] == row3[2]) and ((row1[2] != " ") and (row2[2] != " ") and (row3[2] != " ")):
        if row1[2] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row1[0] == row2[1]) and (row2[1] == row3[2]) and ((row1[0] != " ") and (row2[1] != " ") and (row3[2] != " ")):
        if row1[0] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if (row1[2] == row2[1]) and (row2[1] == row3[0]) and ((row1[2] != " ") and (row2[1] != " ") and (row3[0] != " ")):
        if row1[2] == "X":
            player_2_win = True
        else:
            player_1_win = True
    if player_1_win:
        return "player1 win"
    elif player_2_win:
        return "player2 win"
    else:
        return "no one win"
def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position")
        result = gamechecking()
        if result == "player1 win":
            display(row1, row2, row3)
            print("Player1 win")
            return
        elif result == "player2 win":
            display(row1, row2, row3)
            print("Player2 win")
            return
        elif result == "no one win" and counter == 9:
            display(row1, row2, row3)
            print("Tie game")
            return            
start_game()
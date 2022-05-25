import random
import os
import time

welcome = '''
    ╔╦╦╦═╦╗╔═╦═╦══╦═╗
    ║║║║╚╣╚╣═╣║║║║║╚╣
    ╚══╩═╩═╩═╩═╩╩╩╩═╝
    '''


def print_tic_tac_toe(tic_tac_toe):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tic Tac Toe")
    print()
    print(f'{tic_tac_toe[0][0]} | {tic_tac_toe[0][1]} | {tic_tac_toe[0][2]}')
    print('---------')
    print(f'{tic_tac_toe[1][0]} | {tic_tac_toe[1][1]} | {tic_tac_toe[1][2]}')
    print('---------')
    print(f'{tic_tac_toe[2][0]} | {tic_tac_toe[2][1]} | {tic_tac_toe[2][2]}')

    if tic_tac_toe[0][0] == tic_tac_toe[0][1] == tic_tac_toe[0][2] and tic_tac_toe[0][0] != "":
        print(tic_tac_toe[0][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[1][0] == tic_tac_toe[1][1] == tic_tac_toe[1][2] and tic_tac_toe[1][0] != "":
        print(tic_tac_toe[1][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[2][0] == tic_tac_toe[2][1] == tic_tac_toe[2][2] and tic_tac_toe[2][0] != "":
        print(tic_tac_toe[2][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[0][0] == tic_tac_toe[1][0] == tic_tac_toe[2][0] and tic_tac_toe[0][0] != "":
        print(tic_tac_toe[0][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[0][1] == tic_tac_toe[1][1] == tic_tac_toe[2][1] and tic_tac_toe[0][1] != "":
        print(tic_tac_toe[0][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[0][2] == tic_tac_toe[1][2] == tic_tac_toe[2][2] and tic_tac_toe[0][2] != "":
        print(tic_tac_toe[0][2], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] and tic_tac_toe[0][0] != "":
        print(tic_tac_toe[0][0], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()

    elif tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] and tic_tac_toe[0][2] != "":
        print(tic_tac_toe[0][2], "won the match")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        start_tic_tac_toe()


def start_tic_tac_toe():
    player_x = 'X'
    player_o = 'O'
    tic_tac_toe = [["", "", ""],
                   ["", "", ""],
                   ["", "", ""]]

    game_is_start = True
    while game_is_start:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(welcome)
        user_response = input("For start The game Please enter any key or press q for quit").lower()
        if user_response == 'q':
            game_is_start = False

        for i in range(1, 10):
            if i % 2 != 0:
                player = player_x
                row = random.randint(0, 2)
                column = random.randint(0, 2)
                while tic_tac_toe[row][column] != "":
                    row = random.randint(0, 2)
                    column = random.randint(0, 2)
            else:
                player = player_o
                valid = False
                while not valid:
                    try:
                        row = int(input("user O row: "))
                        column = int(input('user O column: '))
                        valid = True
                    except:
                        print("Please enter valid input")

                while row > 2 or row < 0 or column > 2 or column < 0:
                    print("Please enter coordinates between 0-2")
                    row = int(input("user O row: "))
                    column = int(input('user O column: '))
                while tic_tac_toe[row][column] != "":
                    print("Please enter another coordinates")
                    row = int(input("user O row: "))
                    column = int(input('user O column: '))
            tic_tac_toe[row][column] = player
            print_tic_tac_toe(tic_tac_toe)

        for row in range(3):
            for column in range(3):
                if tic_tac_toe[row][column] != "":
                    print("Draw")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    start_tic_tac_toe()


start_tic_tac_toe()

from tabulate import tabulate
from Check_Move import *
from Speech_Recognition import *

def initial_setup():
    with open('pieces.txt', 'r') as file:
        pieces_list = [pieces.replace('\n', '') for pieces in file]

    for row in 'abcdefgh':
        for column in range(1,9):
            if row == 'a':
                board_dict[f'{row}{column}'] = f'Black {pieces_list[column-1]}'
            elif row == 'b':
                board_dict[f'{row}{column}'] = 'Black Pawn'
            elif row == 'g':
                board_dict[f'{row}{column}'] = 'White Pawn'
            elif row == 'h':
                board_dict[f'{row}{column}'] = f'White {pieces_list[column-1]}'
            else:
                board_dict[f'{row}{column}'] = 'Empty'
    display_board()

def display_board():
    Enter_board = []
    for n in 'abcdefgh':
        Empty_list = [n]
        for key, value in board_dict.items():
            if key[0] == n:
                Empty_list.append(value)
        Enter_board.append(Empty_list)

    print(tabulate(Enter_board, headers=["Index"]+ list('12345678')))

def win():
    if 'White King' not in board_dict.values():
        print('Black Wins')
        speak('Black Wins')
        choice = input('PLay Again?:')
        if choice.lower() == 'yes':
            initial_setup()
            return False
        else:
            return True
    elif 'Black King' not in board_dict.values():
        print('White Wins')
        speak('White Wins')
        choice = input('PLay Again?:')
        if choice.lower() == 'yes':
            initial_setup()
            return False
        else:
            return True
    else:
        return False

def checkmate():
    color = ['Black', 'White']
    result = [[],[]]
    key_list = list(board_dict.keys())
    value_list = list(board_dict.values())
    for i in range(2):
            pcolor = color[i]
            king_position = key_list[value_list.index(f'{color[(i+1)%2]} King')]
            for key,value in board_dict.items():
                if value == f'{pcolor} Rook':
                    result[i].append(Rook_Move(key, king_position, board_dict))
                if value == f'{pcolor} Pawn':
                    result[i].append(Pawn_Move(key, king_position, board_dict))
                if value == f'{pcolor} Knight':
                    result[i].append(Knight_Move(key,king_position,board_dict))
                if value == f'{pcolor} Bishop':
                    result[i].append(Bishop_Move(key, king_position, board_dict))
                if value == f'{pcolor} Queen':
                    result[i].append(Queen_Move(key, king_position, board_dict))
                if value == f'{pcolor} King':
                    result[i].append(King_Move(key, king_position, board_dict))
    if True in result[0]:
        print('Black Checkmate')
        speak('Black Checkmate')
    if True in result[1]:
        print('White Checkmate')
        speak(('White Checkmate'))


def move():
    global wrong_turn, exit, reset, speech_end, speech_start
    start = input('Enter Position of Moving Piece: ').lower()
    if start.lower() == 'reset':
        initial_setup()
        reset = True
        wrong_turn = False
    if start.lower() == 'exit':
        exit = True
        wrong_turn = False
    if not reset and not exit:
        end = input('Enter Where you want to Move it to: ').lower()
        if end.lower() == 'reset':
            initial_setup()
            reset = True
            wrong_turn = False
        if end.lower() == 'exit':
            exit = True
            wrong_turn = False
        if start[0].isdigit():
            start = start[::-1]
        if end[0].isdigit():
            end = end[::-1]
        flag = False
        if not reset and not exit and board_dict[end][0] != board_dict[start][0] and turn[i%2][0] == board_dict[start][0]:
            if 'Pawn' in board_dict[start]:
                flag = Pawn_Move(start, end, board_dict)
            if 'Rook' in board_dict[start]:
                flag = Rook_Move(start, end, board_dict)
            if 'Knight' in board_dict[start]:
                flag = Knight_Move(start,end,board_dict)
            if 'Bishop' in board_dict[start]:
                flag = Bishop_Move(start, end, board_dict)
            if 'Queen' in board_dict[start]:
                flag = Queen_Move(start, end, board_dict)
            if 'King' in board_dict[start]:
                flag = King_Move(start, end, board_dict)
            wrong_turn = False

        if flag:
            speech_end = board_dict[end]
            speech_start = board_dict[start]
            board_dict[end] = board_dict[start]
            board_dict[start] = 'Empty'
        else:
            if not reset and not exit and not wrong_turn:
                print('\nInvalid Move\n')
                speak('Invalid Move')
                global invalid_move
                invalid_move = True

        if not reset and not exit:
            display_board()
        if flag:
            if speech_end != 'Empty':
                speak(f'You Moved {speech_start} from {start} to {end} and Killed {speech_end}')
            elif speech_end == 'Empty':
                speak(f'You Moved {speech_start} from {start} to {end}')



board_dict = dict()

print('\nWelcome to Chess')
speak('Welcome to Chess')
print('\n\nTips: Enter "exit" to quit game or "reset" to restart game\n\n')
speak('Press Enter to Play')
enter = input('Press Enter to Play')


initial_setup()

turn = ['Black', 'White']
i = 0
while not win():
    print(f'\n{turn[i%2]}\'s Turn\n')
    speak(f'{turn[i%2]}\'s Turn')
    wrong_turn = True
    invalid_move = False
    exit = False
    reset = False
    checkmate()
    move()
    if exit:
        print('\nGood Bye!\n')
        speak('Good Bye')
        break
    if invalid_move:
        pass
    elif not reset and not exit and not wrong_turn:
        i += 1
    elif not reset and not exit:
        print('\nWrong Turn\n')
        speak('Wrong Turn')





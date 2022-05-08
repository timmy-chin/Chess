from tabulate import tabulate
from Check_Move import *
from Speech_Recognition import *


def initial_setup():
    with open('pieces.txt', 'r') as file:
        pieces_list = [pieces.replace('\n', '') for pieces in file]

    for row in 'abcdefgh':
        for column in range(1, 9):
            if row == 'a':
                board_dict[f'{row}{column}'] = f'Black {pieces_list[column - 1]}'
            elif row == 'b':
                board_dict[f'{row}{column}'] = 'Black Pawn'
            elif row == 'g':
                board_dict[f'{row}{column}'] = 'White Pawn'
            elif row == 'h':
                board_dict[f'{row}{column}'] = f'White {pieces_list[column - 1]}'
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

    print(tabulate(Enter_board, headers=["Index"] + list('12345678')))


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


def check_or_checkmate():
    color = ['Black', 'White']
    checker = []
    checker_path = []
    king_positions = []
    key_list = list(board_dict.keys())
    value_list = list(board_dict.values())
    for i in range(2):
        pcolor = color[i]
        king_position = key_list[value_list.index(f'{color[(i + 1) % 2]} King')]
        king_positions.append(king_position)
        getpath = True
        for key, value in board_dict.items():
            if value == f'{pcolor} Rook':
                result = Rook_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} Rook')
                    checker_path.append(Rook_Move(key, king_position, board_dict, getpath))
            if value == f'{pcolor} Pawn':
                result = Pawn_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} Pawn')
                    checker_path.append(Pawn_Move(key, king_position, board_dict, getpath))
            if value == f'{pcolor} Knight':
                result = Knight_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} Knight')
                    checker_path.append(Knight_Move(key, king_position, board_dict, getpath))
            if value == f'{pcolor} Bishop':
                result = Bishop_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} Bishop')
                    checker_path.append(Bishop_Move(key, king_position, board_dict, getpath))
            if value == f'{pcolor} Queen':
                result = Queen_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} Queen')
                    checker_path.append(Queen_Move(key, king_position, board_dict, getpath))
            if value == f'{pcolor} King':
                result = King_Move(key, king_position, board_dict)
                if result:
                    checker.append(f'{pcolor} King')
                    checker_path.append(King_Move(key, king_position, board_dict, getpath))

    Black = False
    White = False
    White_CheckMate = False
    Black_CheckMate = False
    for piece in checker:
        if 'Black' in piece:
            Black = True
        if 'White' in piece:
            White = True
    if checker != []:
        if White and Black:
            White_CheckResults = [white_not_checkmate(checker_path[i],board_dict,king_positions) for i in range(len(checker)) if 'White' in checker[i]]
            Black_CheckResults = [black_not_checkmate(checker_path[i], board_dict, king_positions) for i in range(len(checker)) if 'Black' in checker[i]]
            if False in White_CheckResults:
                White_CheckMate = True
            if False in Black_CheckResults:
                Black_CheckMate = True
        elif White:
            White_CheckResults = [white_not_checkmate(checker_path[i],board_dict,king_positions) for i in range(len(checker)) if 'White' in checker[i]]
            if False in White_CheckResults:
                White_CheckMate = True

        elif Black:
            Black_CheckResults = [black_not_checkmate(checker_path[i], board_dict, king_positions) for i in range(len(checker)) if 'Black' in checker[i]]
            if False in Black_CheckResults:
                Black_CheckMate = True


        if White and White_CheckMate:
            print('White Checkmate')
            speak('White Checkmate')
        elif Black and Black_CheckMate:
            print('Black Checkmate')
            speak('Black Checkmate')
        elif Black and White and not White_CheckMate and not White_CheckMate:
            print('Black Check and White Check')
            speak('Black Check and White Check')
        elif Black and not Black_CheckMate:
            print('Black Check')
            speak('Black Check')
        elif White and not White_CheckMate:
            print('White Check')
            speak('White Check')



def white_not_checkmate(path_list, board_dict, king_positions):

    for path in path_list:
        for key, value in board_dict.items():
            if 'Black Rook' in value:
                if Rook_Move(key, path, board_dict):
                    return True
            if 'Black Pawn' in value:
                if Pawn_Move(key, path, board_dict):
                    return True
            if 'Black Knight' in value:
                if Knight_Move(key, path, board_dict):
                    return True
            if 'Black Bishop' in value:
                if Bishop_Move(key, path, board_dict):
                    return True
            if 'Black Queen' in value:
                if Queen_Move(key, path, board_dict):
                    return True

    king_position = king_positions[1]
    init_letter = ord(king_position[0])
    init_num = int(king_position[1])
    check_king_paths = [f'{chr(init_letter + 1)}{init_num + 1}', f'{chr(init_letter - 1)}{init_num - 1}', f'{chr(init_letter - 1)}{init_num + 1}', f'{chr(init_letter + 1)}{init_num - 1}',
                        f'{chr(init_letter + 1)}{init_num}', f'{chr(init_letter - 1)}{init_num}', f'{chr(init_letter)}{init_num + 1}', f'{chr(init_letter)}{init_num - 1}' ]
    result = []
    for end in check_king_paths:
        if ord('a') <= ord(end[0]) <= ord('h') and 1 <= int(end[1]) <= 8:
            if King_Move(king_position, end, board_dict):
                result.append(Saved(end, 'White', board_dict))
    if True in result:
        return True

    return False

def black_not_checkmate(path_list, board_dict, king_positions):


    for path in path_list:
        for key, value in board_dict.items():
            if 'White Rook' in value:
                if Rook_Move(key, path, board_dict):
                    return True
            if 'White Pawn' in value:
                if Pawn_Move(key, path, board_dict):
                    return True
            if 'White Knight' in value:
                if Knight_Move(key, path, board_dict):
                    return True
            if 'White Bishop' in value:
                if Bishop_Move(key, path, board_dict):
                    return True
            if 'White Queen' in value:
                if Queen_Move(key, path, board_dict):
                    return True

    king_position = king_positions[0]
    init_letter = ord(king_position[0])
    init_num = int(king_position[1])
    check_king_paths = [f'{chr(init_letter + 1)}{init_num + 1}', f'{chr(init_letter - 1)}{init_num - 1}', f'{chr(init_letter - 1)}{init_num - 1}', f'{chr(init_letter + 1)}{init_num - 1}',
                        f'{chr(init_letter + 1)}{init_num}', f'{chr(init_letter - 1)}{init_num}', f'{chr(init_letter)}{init_num + 1}', f'{chr(init_letter)}{init_num - 1}' ]
    result = []
    for end in check_king_paths:
        if ord('a') <= ord(end[0]) <= ord('h') and 1 <= int(end[1]) <= 8:
            if King_Move(king_position, end, board_dict):
                result.append(Saved(end, 'Black', board_dict))
    if True in result:
        return True

    return False




def Saved(king_position, enemy_color, board_dict):
    mirror_dimension = dict(board_dict)
    mirror_dimension[king_position] = 'Empty'
    for key, value in mirror_dimension.items():
        if value == f'{enemy_color} Rook':
            if Rook_Move(key, king_position, mirror_dimension):
                return False
        if value == f'{enemy_color} Pawn':
            if Pawn_Move(key, king_position, mirror_dimension):
                return False
        if value == f'{enemy_color} Knight':
            if Knight_Move(key, king_position, mirror_dimension):
                return False
        if value == f'{enemy_color} Bishop':
            if Bishop_Move(key, king_position, mirror_dimension):
                return False
        if value == f'{enemy_color} Queen':
            if Queen_Move(key, king_position, mirror_dimension):
                return False
        if value == f'{enemy_color} King':
            if King_Move(key, king_position, mirror_dimension):
                return False
    else:
        return True


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
        if not reset and not exit and board_dict[end][0] != board_dict[start][0] and turn[i % 2][0] == \
                board_dict[start][0]:
            if 'Pawn' in board_dict[start]:
                flag = Pawn_Move(start, end, board_dict)
            if 'Rook' in board_dict[start]:
                flag = Rook_Move(start, end, board_dict)
            if 'Knight' in board_dict[start]:
                flag = Knight_Move(start, end, board_dict)
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

# with open('Checkmate_Test.txt', 'r') as file:
#     test_case = [move.replace('\n', '') for move in file]

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
    print(f'\n{turn[i % 2]}\'s Turn\n')
    speak(f'{turn[i % 2]}\'s Turn')
    wrong_turn = True
    invalid_move = False
    exit = False
    reset = False
    check_or_checkmate()
    try:
        move()
    except:
        print('SLOW DOWN!!')
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

from tabulate import tabulate
from Check_Move import *
from Check_Kill import *

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
        return True
    elif 'Black King' not in board_dict.values():
        print('White Wins')
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
                    result[i].append(Rook_Kill(key,king_position,board_dict))
                if value == f'{pcolor} Pawn':
                    result[i].append(Pawn_Kill(key,king_position,board_dict))
                if value == f'{pcolor} Knight':
                    result[i].append(Knight_Move(key,king_position,board_dict))
                if value == f'{pcolor} Bishop':
                    result[i].append(Bishop_Kill(key,king_position,board_dict))
                if value == f'{pcolor} Queen':
                    result[i].append(Queen_Kill(key,king_position,board_dict))
                if value == f'{pcolor} King':
                    result[i].append(King_Kill(key,king_position,board_dict))
    if True in result[0]:
        print('Black Checkmate White')
        print(result[0])
    if True in result[1]:
        print('White Checkmate Black')
        print(result[1])


def move():
    start = input('Enter Position of Moving Piece: ').lower()
    end = input('Enter Where you want to Move it to: ').lower()
    reset = False
    if start == 'reset' or end == 'reset':
        initial_setup()
        reset = True
    if start[0].isdigit():
        start = start[::-1]
    if end[0].isdigit():
        end = end[::-1]
    flag = False
    if board_dict[end] != 'Empty' and board_dict[end][0] != board_dict[start][0]:
        flag = False
        if 'Pawn' in board_dict[start]:
            flag = Pawn_Kill(start,end,board_dict)
        if 'Rook' in board_dict[start]:
            flag = Rook_Kill(start,end,board_dict)
        if 'Knight' in board_dict[start]:
            flag = Knight_Move(start,end,board_dict)
        if 'Bishop' in board_dict[start]:
            flag = Bishop_Kill(start,end,board_dict)
        if 'Queen' in board_dict[start]:
            flag = Queen_Kill(start,end,board_dict)
        if 'King' in board_dict[start]:
            flag = King_Kill(start,end,board_dict)
    elif board_dict[end] == 'Empty':
        if 'Rook' in board_dict[start]:
            flag = Rook_Move(start,end, board_dict)
        if 'Pawn' in board_dict[start]:
            flag = Pawn_Move(start, end, board_dict)
        if 'Knight' in board_dict[start]:
            flag = Knight_Move(start, end, board_dict)
        if 'Bishop' in board_dict[start]:
            flag = Bishop_Move(start, end, board_dict)
        if 'Queen' in board_dict[start]:
            flag = Queen_Move(start,end,board_dict)
        if 'King' in board_dict[start]:
            flag = King_Move(start, end, board_dict)
    else:
        if not reset:
            print('Invalid Move')

    if flag:
        board_dict[end] = board_dict[start]
        board_dict[start] = 'Empty'
    display_board()


board_dict = dict()

initial_setup()

while not win():
    move()
    # checkmate()





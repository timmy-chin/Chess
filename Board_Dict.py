from tabulate import tabulate
from Check_Move import *

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

def move():
    start = input('Enter Position of Moving Piece: ').lower()
    end = input('Enter Where you want to Move it to: ').lower()
    if start[0].isdigit():
        start = start[::-1]
    if end[0].isdigit():
        end = end[::-1]
    flag = False
    if 'Rook' in board_dict[start]:
        flag = Rook_Move(start,end, board_dict)
    if 'Pawn' in board_dict[start]:
        flag = Pawn_Move(start, end, board_dict)
    if 'Knight' in board_dict[start]:
        flag = Knight_Move(start, end, board_dict)
    if 'Bishop' in board_dict[start]:
        flag = Bishop_Move(start, end, board_dict)


    if flag:
        board_dict[end] = board_dict[start]
        board_dict[start] = 'Empty'
    display_board()


board_dict = dict()


initial_setup()

while True:
    move()





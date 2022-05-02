def Rook_Move(start, end, board_dict):
    if start[0] == end[0]:
        for i in range(int(start[1]),int(end[1])):
            if board_dict[f'{start[0]}{i+1}'] != 'Empty':
                print('Invalid Move')
                return False
        return True
    elif start[1] == end[1]:
        init_letter = ord(start[0])
        final_letter = ord(end[0])
        for i in range(init_letter,final_letter):
            if board_dict[f'{chr(i+1)}{start[1]}'] != 'Empty':
                print('Invalid Move')
                return False
        return True
    else:
        print('Invalid Move')
        return False

def Pawn_Move(start, end, board_dict):
    if start[0] == 'b' and end[0] == 'd':
        init_letter = ord(start[0])
        final_letter = ord(end[0])
        for i in range(init_letter,final_letter):
            if board_dict[f'{chr(i+1)}{start[1]}'] != 'Empty':
                print('Invalid Move')
                return False
            return True
    elif start[1] == end[1] and (ord(end[0])-ord(start[0])) == 1:
        if board_dict[end] != 'Empty':
            print('Invalid Move')
            return False
        return True
    else:
        print('Invalid Move')
        return False

def Knight_Move(start, end, board_dict):
    init_letter = ord(start[0])
    final_letter = ord(end[0])
    if chr(init_letter+1) == chr(final_letter) and abs(int(start[1]) - int(end[1])) == 2:
        if board_dict[end] != 'Empty':
            print('Invalid Move')
            return False
        return True
    elif chr(init_letter+2) == chr(final_letter) and abs(int(start[1]) - int(end[1])) == 1:
        if board_dict[end] != 'Empty':
            print('Invalid Move')
            return False
        return True
    else:
        print('Invalid Move')
        return False

def Bishop_Move(start, end, board_dict):
    init_letter = ord(start[0])
    final_letter = ord(end[0])
    init_num = int(start[1])
    for i in range(-8,8):
        if ord('a') <= init_letter+i <= ord('h') and 0 < init_num + i <= 8:
            if f'{chr(init_letter+i)}{init_num+i}' == end:
                distance = abs(int(end[1]) - int(start[1]))
                if start[1] < end[1]:
                    for i in range(distance):
                        if board_dict[f'{chr(init_letter+i+1)}{init_num+i+1}'] != 'Empty':
                            print('Invalid Move')
                            return False
                        return True
                elif start[1] > end[1]:
                    for i in range(distance):
                        if board_dict[f'{chr(init_letter-i-1)}{init_num-i-1}'] != 'Empty':
                            print('Invalid Move')
                            return False
                        return True
            elif f'{chr(init_letter + i)}{init_num - i}' == end:
                distance = abs(int(end[1]) - int(start[1]))
                if start[1] < end[1]:
                    for i in range(distance):
                        if board_dict[f'{chr(init_letter - i - 1)}{init_num + i + 1}'] != 'Empty':
                            print('Invalid Move')
                            return False
                        return True
                elif start[1] > end[1]:
                    for i in range(distance):
                        if board_dict[f'{chr(init_letter + i + 1)}{init_num - i - 1}'] != 'Empty':
                            print('Invalid Move')
                            return False
                        return True
    else:
        print('Invalid Move')
        return False

def Queen_Move(start, end, board_dict):
    if start[0] == end[0]:
        for i in range(int(start[1]),int(end[1])):
            if board_dict[f'{start[0]}{i+1}'] != 'Empty':
                print('Invalid Move')
                return False
        return True
    elif start[1] == end[1]:
        init_letter = ord(start[0])
        final_letter = ord(end[0])
        for i in range(init_letter,final_letter):
            if board_dict[f'{chr(i+1)}{start[1]}'] != 'Empty':
                print('Invalid Move')
                return False
        return True
    else:
        Bishop_Move(start,end,board_dict)






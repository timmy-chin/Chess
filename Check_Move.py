def Pawn_Move(start, end, board_dict, getpath=False):
    init_letter = ord(start[0])
    init_num = int(start[1])
    if getpath:
        return [start]
    if board_dict[end] != 'Empty' and (f'{chr(init_letter + 1)}{init_num + 1}' == end or f'{chr(init_letter - 1)}{init_num - 1}' == end or f'{chr(init_letter - 1)}{init_num + 1}' == end or f'{chr(init_letter + 1)}{init_num - 1}' == end):
        return True
    if start[0] == 'b' and end[0] == 'd' and 'Black' in board_dict[start] and start[1] == end[1]:
        init_letter = ord(start[0])
        for i in range(1,3):
            if board_dict[f'{chr(init_letter+i)}{start[1]}'] != 'Empty':
                return False
        return True
    elif start[0] == 'g' and end[0] == 'e' and start[1] == end[1]:
        init_letter = ord(start[0])
        for i in range(1,3):
            if board_dict[f'{chr(init_letter-i)}{start[1]}'] != 'Empty':
                return False
        return True
    elif start[1] == end[1] and abs((ord(end[0])-ord(start[0]))) == 1:
        if board_dict[end] != 'Empty':
            return False
        return True
    else:
        return False

def Rook_Move(start, end, board_dict, getpath=False):
    path = [start]
    if start[0] == end[0]:
        distance = abs(int(start[1]) - int(end[1]))
        if getpath and distance == 1:
            return path
        if distance == 1:
            return True
        elif end[1] > start[1]:
            for i in range(1,distance):
                path.append(f'{start[0]}{int(start[1])+i}')
                if board_dict[f'{start[0]}{int(start[1])+i}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
        elif end[1] < start[1]:
            for i in range(1,distance):
                path.append(f'{start[0]}{int(start[1])-i}')
                if board_dict[f'{start[0]}{int(start[1])-i}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
    elif start[1] == end[1]:
        init_letter = ord(start[0])
        final_letter = ord(end[0])
        distance = abs(final_letter - init_letter)
        if getpath and distance == 1:
            return path
        if distance == 1:
            return True
        elif final_letter > init_letter:
            for i in range(1,distance):
                path.append(f'{chr(init_letter + i)}{start[1]}')
                if board_dict[f'{chr(init_letter + i)}{start[1]}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
        elif final_letter < init_letter:
            for i in range(1,distance):
                path.append(f'{chr(init_letter - i)}{start[1]}')
                if board_dict[f'{chr(init_letter - i)}{start[1]}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
    else:
        return False

def Bishop_Move(start, end, board_dict, getpath=False):
    path = [start]
    init_letter = ord(start[0])
    init_num = int(start[1])
    for i in range(-8,8):
        if ord('a') <= init_letter+i <= ord('h') and 0 < init_num + i <= 8:
            if f'{chr(init_letter+i)}{init_num+i}' == end:
                distance = abs(int(end[1]) - int(start[1]))
                if getpath and distance == 1:
                    return path
                if distance == 1:
                    return True
                elif start[1] < end[1]:
                    for n in range(1,distance):
                        path.append(f'{chr(init_letter+n)}{init_num+n}')
                        if board_dict[f'{chr(init_letter+n)}{init_num+n}'] != 'Empty':
                            return False
                    if getpath:
                        return path
                    return True
                elif start[1] > end[1]:
                    for i in range(1, distance):
                        path.append(f'{chr(init_letter-i)}{init_num-i}')
                        if board_dict[f'{chr(init_letter-i)}{init_num-i}'] != 'Empty':
                            return False
                    if getpath:
                        return path
                    return True
        elif ord('a') <= init_letter + i <= ord('h') and 0 < init_num - i <= 8:
            if f'{chr(init_letter + i)}{init_num - i}' == end:
                distance = abs(int(end[1]) - int(start[1]))
                if getpath and distance == 1:
                    return path
                if distance == 1:
                    return True
                elif start[1] < end[1]:
                    for i in range(1, distance):
                        path.append(f'{chr(init_letter - i)}{init_num + i}')
                        if board_dict[f'{chr(init_letter - i)}{init_num + i}'] != 'Empty':
                            return False
                    if getpath:
                        return path
                    return True
                elif start[1] > end[1]:
                    for i in range(1, distance):
                        path.append(f'{chr(init_letter + i)}{init_num - i}')
                        if board_dict[f'{chr(init_letter + i)}{init_num - i}'] != 'Empty':
                            return False
                    if getpath:
                        return path
                    return True
    else:
        return False

def Queen_Move(start, end, board_dict, getpath=False):
    path = [start]
    if start[0] == end[0]:
        distance = abs(int(start[1]) - int(end[1]))
        if getpath and distance == 1:
            return path
        if distance == 1:
            return True
        elif end[1] > start[1]:
            for i in range(1,distance):
                path.append(f'{start[0]}{int(start[1])+i}')
                if board_dict[f'{start[0]}{int(start[1])+i}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
        elif end[1] < start[1]:
            for i in range(1,distance):
                path.append(f'{start[0]}{int(start[1])-i}')
                if board_dict[f'{start[0]}{int(start[1])-i}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
    elif start[1] == end[1]:
        init_letter = ord(start[0])
        final_letter = ord(end[0])
        distance = abs(final_letter - init_letter)
        if getpath and distance == 1:
            return path
        if distance == 1:
            return True
        elif final_letter > init_letter:
            for i in range(1,distance):
                path.append(f'{chr(init_letter + i)}{start[1]}')
                if board_dict[f'{chr(init_letter + i)}{start[1]}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
        elif final_letter < init_letter:
            for i in range(1,distance):
                path.append(f'{chr(init_letter - i)}{start[1]}')
                if board_dict[f'{chr(init_letter - i)}{start[1]}'] != 'Empty':
                    return False
            if getpath:
                return path
            return True
    else:
        return Bishop_Move(start, end, board_dict, getpath=False)

def King_Move(start, end, board_dict, getpath=False):
    init_letter = ord(start[0])
    init_num = int(start[1])
    if getpath:
        return [start]
    if start[1] == end[1] and abs((ord(end[0])-ord(start[0]))) == 1:
        return True
    elif start[0] == end[0] and abs(int(start[1]) - int(end[1])) == 1:
        return True
    elif f'{chr(init_letter + 1)}{init_num + 1}' == end or f'{chr(init_letter - 1)}{init_num - 1}' == end or f'{chr(init_letter + 1)}{init_num - 1}' == end or  f'{chr(init_letter - 1)}{init_num + 1}' == end:
        return True
    else:
        return False

def Knight_Move(start, end, board_dict, getpath=False):
    init_letter = ord(start[0])
    final_letter = ord(end[0])
    if getpath:
        return [start]
    if (chr(init_letter+1) == chr(final_letter) or chr(init_letter-1) == chr(final_letter)) and abs(int(start[1]) - int(end[1])) == 2:
        return True
    elif (chr(init_letter+2) == chr(final_letter) or chr(init_letter-2) == chr(final_letter)) and abs(int(start[1]) - int(end[1])) == 1:
        return True
    else:
        return False
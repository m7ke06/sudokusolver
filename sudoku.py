digits = [1,2,3,4,5,6,7,8,9]
digits_inline = [0 for i in range(9)]
digits_line = 0
digits_incolumn = [0 for i in range(9)]
digits_column = 0
digits_insquare = [0 for i in range(9)]
digits_square = 0
exact_digits_inSquare = [[0 for i in range(9)] for j in range(9)]
rotated = [[0 for i in range(9)] for j in range(9)]
same = [[0 for i in range(9)] for j in range(9)]
missing_line = [0 for i in range(9)]
missing_line_without = [0 for i in range(9)]
missing_column = [0 for i in range(9)]
zeros = [0 for i in range(9)]
again = 1
counter1 = 0

putin = [ [0,2,0,0,8,0,0,3,0],
          [3,0,0,0,7,0,0,0,0],
          [0,0,0,0,0,0,1,9,0],
          [0,0,6,2,4,0,0,0,0],
          [0,0,0,0,0,0,0,0,1],
          [2,0,8,0,3,6,0,0,0],
          [4,0,0,0,6,0,0,0,0],
          [5,0,2,4,0,0,0,0,0],
          [0,6,0,0,9,7,8,0,4],]     # input SUDOKU

def Fill(putin, rotated):
    for i in range(9):
        for j in range(9):
            rotated[j][i] = putin[i][j]

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif

def Intersection(lst1, lst2):
    lst3 =  [value for value in lst1 if value in lst2]
    return lst3

def Trying():
    global same
    while True:
        
        for i in range(9):
            digits_line = 0
            for j in range(9):
                if putin[i][j] != 0:
                    digits_line = digits_line + 1
            digits_inline[i] = digits_line

        for i in range(9):
            digits_column = 0
            for j in range(9):
                if putin[j][i] != 0:
                    digits_column = digits_column + 1
            digits_incolumn[i] = digits_column


        for i in range(9):
            if digits_inline[i] == 8:
                special = Diff(digits,putin[i])
                special.remove(0)
                special_integer = int(special[0])
                for j in range(9):
                    if putin[i][j] == 0:
                        putin[i][j] = special_integer
                        break
        Fill(putin,rotated)

        for i in range(9):
            if digits_incolumn[i] == 8:
                special = Diff(digits,rotated[i])
                if 0 in special:
                    special.remove(0)
                    special_integer = int(special[0])
                    for j in range(9):
                        if putin[j][i] == 0:
                            putin[j][i] = special_integer
                            break
        Fill(putin,rotated)
        # Numbers in little squares
        for k in range(3):
            for l in range(3):
                digits_square = 0
                for i in range(3):
                    for j in range(3):
                        if putin[i+(k*3)][j+(l*3)] != 0:
                            digits_square += 1
                        exact_digits_inSquare[l+(k*3)][j+(i*3)] = putin[i+(k*3)][j+(l*3)]
                digits_insquare[l+(k*3)] = digits_square
                if digits_insquare[l+(k*3)] == 8:
                    special = Diff(digits, exact_digits_inSquare[l+(k*3)])
                    special_integer = int(special[0])
                    for i in range(3):
                        for j in range(3):
                            if putin[i+(k*3)][j+(l*3)] == 0:
                                putin[i+(k*3)][j+(l*3)] = special_integer
        
        Fill(putin, rotated)
                    
        if same == rotated:
            break
        same = rotated

def Missing():
    # What's missing in lines
    for i in range(9):
        special = Diff(digits,putin[i])
        b = 0
        for _ in range(len(special)):
            if special[b] == 0:
                del special[b]
                b -= 1
            b += 1
        missing_line[i] = special
    # What's missing in columns
    for i in range(9):
        special = Diff(digits, rotated[i])
        b = 0
        for _ in range(len(special)):
            if special[b] == 0:
                del special[b]
                b -= 1
            b += 1
        missing_column[i] = special

Trying()
Missing()

while again > 0:
    again = 0
    for i in range(9):
        for j in range(9):
            if putin[i][j] == 0:
                a = missing_line[i]
                b = missing_column[j]
                c = Intersection(a,b)
                counter1 = 0
                for _ in range(len(c)):
                    if (c[counter1] in exact_digits_inSquare[0]) and (i <= 2 and j <= 2):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[1]) and (i <= 2 and j > 2 and j <= 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[2]) and (i <= 2 and j > 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[3]) and (i > 2 and i <= 5 and j <= 2):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[4]) and (i > 2 and i <= 5 and j > 2 and j <= 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[5]) and (i > 2 and i <= 5 and j > 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[6]) and (i > 5 and j <= 2):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[7]) and (i > 5 and j > 2 and j <= 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    elif (c[counter1] in exact_digits_inSquare[8]) and (i > 5 and j > 5):
                        c.remove(c[counter1])
                        counter1 = counter1 - 1
                    counter1 = counter1 + 1

                if len(c) == 1:
                    d = c[0]
                    putin[i][j] = d

    Trying()
    Missing()
    for i in range(9):
        for j in range(9):
            if putin[i][j] == 0:
                again = 1
                
    for i in range(9):
        print(putin[i])
    print("////////////////////////////////////")
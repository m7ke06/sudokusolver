digits = [1,2,3,4,5,6,7,8,9]
digits_inline = [0 for i in range(9)]
digits_line = 0
digits_incolumn = [0 for i in range(9)]
digits_column = 0
digits_insquare = [0 for i in range(9)]
digits_square = 0
rotated = [[0 for i in range(9)] for j in range(9)]
same = [[0 for i in range(9)] for j in range(9)]
missing_line = [0 for i in range(9)]
missing_column = [0 for i in range(9)]
zeros = [0 for i in range(9)]
again = 1

putin = [ [7,0,3,6,1,2,0,0,0],
          [0,0,1,0,0,0,3,0,0],
          [8,4,2,0,9,0,7,0,6],
          [0,7,0,0,4,1,5,3,2],
          [0,0,0,9,2,6,0,0,0],
          [4,2,8,7,5,0,0,6,0],
          [2,0,4,0,3,0,8,5,7],
          [0,0,7,0,0,0,2,0,0],
          [0,0,0,2,7,8,6,0,3],]     # input SUDOKU

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

# Filling part
def Trying():
    global same
    while True:
        
        for i in range(9):
            digits_line = 0
            for j in range(9):
                if putin[i][j] != 0:
                    digits_line += digits_line
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
        Fill(putin,rotated)
        # Numbers in little squares
        for k in range(3):
            for l in range(3):
                digits_square = 0
                for i in range(3):
                    for j in range(3):
                        if putin[i+(k*3)][j+(l*3)] != 0:
                            digits_square += 1
                digits_insquare[l+(k*3)] = digits_square
                print(digits_insquare[l+(k*3)])
                # if digits_insquare[i] == 8:
                    


        if same == rotated:
            break
        
        same = rotated
Trying()
# for i in range(9):
#     print(putin[i])
# /Filling part

# Guessing part
for i in range(9):
    special = Diff(digits,putin[i])
    b = 0
    for j in range(len(special)):
        if special[b] == 0:
            del special[b]
            b -= 1
        b += 1
    missing_line[i] = special

# print(missing_line)

for i in range(9):
    special = Diff(digits, rotated[i])
    b = 0
    for j in range(len(special)):
        if special[b] == 0:
            del special[b]
            b -= 1
        b += 1
    missing_column[i] = special
# print(missing_column)
while again > 0:
    again = 0
    for i in range(9):
        for j in range(9):
            if putin[i][j] == 0:
                a = missing_line[i]
                b = missing_column[j]
                c = Intersection(a,b)
                if len(c) == 1:
                    d = c[0]
                    putin[i][j] = d
                    Trying()
    Trying()
    for i in range(9):
        for j in range(9):
            if putin[i][j] == 0:
                again = 1
    print('///////////////////////')
    for i in range(9):
        print(putin[i])
            


    

         


digits = [1,2,3,4,5,6,7,8,9]
digits_inline = [0 for i in range(9)]
digits_line = 0
digits_incolumn = [0 for i in range(9)]
digits_column = 0
rotated = [[0 for i in range(9)] for j in range(9)]
same = [[0 for i in range(9)] for j in range(9)]
missing_line = [0 for i in range(9)]

putin = [ [0,2,0,4,5,6,7,8,9],
          [4,5,7,0,8,0,2,3,6],
          [6,8,9,2,3,7,0,4,0],
          [0,0,5,3,6,2,9,7,4],
          [2,7,4,0,9,0,6,5,3],
          [3,9,6,5,7,4,8,0,0],
          [0,4,0,6,1,8,3,9,7],
          [7,6,1,0,4,0,5,2,8],
          [9,3,8,7,2,5,0,6,0],]     # input SUDOKU

# Filling part
def Fill(putin, rotated):
    for i in range(9):
        for j in range(9):
            rotated[j][i] = putin[i][j]

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

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
    if same == rotated:
        break
    
    same = rotated

for i in range(9):
    print(putin[i])
# /Filling part

# Guessing part
for i in range(9):
    special = Diff(digits,putin[i])
    for j in range(len(special)):
        if special[j-1] == 0:
            del special[j-1]
    missing_line[i] = special

print(missing_line)
            


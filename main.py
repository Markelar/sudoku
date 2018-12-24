from Sudoku import Sudoku
import sys
import json

print("||------------------------------------------||\n||                                          ||\n||        Super Smooth Sudoku Solver        ||\n||                                          ||\n||------------------------------------------||\n")
print("Please insert the numbers of your Sudoku, seperated by a comma. Use \"0\" for empty values.\n")

values = {}
counter = 1

input_values = []

def user_input_values():
    try:
        return raw_input().split(",")
    except ValueError:
        print("Please insert the numbers of your Sudoku, seperated by a comma. Use \"0\" for empty values.\n")
    except KeyboardInterrupt:
        sys.exit()

c = True
while c:
    input_values = user_input_values()

    def check_type(input_values, counter):
        for value in input_values:
            try:
                val = int(value)
            except ValueError:
                print("Please insert only numbers.\n")
                return False
                
            values[counter] = value
            counter += 1
        return True

    def check_length(input_values):
        if(len(input_values) != 81):
            print("There are numbers missing. Please insert all values of your Sudoku.\n")
            input_values = []
            return False
        return True

    if(check_type(input_values, counter)):
        if(check_length(input_values)):
            c = False
            continue
    else:
        continue

sudoku = Sudoku(values)
single_values = sudoku.single_values
row_values = {}
column_values = {}
square_values = {}
for i in range(9):
    row_values[i+1] = {}
    column_values[i+1] = {}
    square_values[i+1] = {}

empty_values_indices = []

#assigning values, filling dicts
for index in single_values:
    row = single_values[index].row
    column = single_values[index].column
    square = single_values[index].square

    row_values[row][index] = single_values[index]
    column_values[column][index] = single_values[index]
    square_values[square][index] = single_values[index]

#detecting possible values by comparing with other values from the same row, column, square
def calc_possible_values():
    for index in single_values:
        if(int(single_values[index].final_value) == 0):
            empty_values_indices.append(int(index))
        else:
            continue
        row = single_values[index].row
        column = single_values[index].column
        square = single_values[index].square
        v = int(single_values[index].final_value)

        if(v == 0):
            possible_values = ['1','2','3','4','5','6','7','8','9']
        else:
            possible_values = []
            continue

        for r in row_values[row]:
            blocking_value = row_values[row][r].final_value
            if(str(blocking_value) in possible_values):
                possible_values.remove(blocking_value)
                    
    
        for c in column_values[column]:
            blocking_value = column_values[column][c].final_value
            if(blocking_value in possible_values):
                possible_values.remove(blocking_value)

        for s in square_values[square]:
            blocking_value = square_values[square][s].final_value
            if(blocking_value in possible_values):
                possible_values.remove(blocking_value)

        single_values[index].possible_values = possible_values

#calculating the sudoku
c = True
while c:
    c = False

    calc_possible_values()

    for x in empty_values_indices[:]:
        pv = single_values[x].possible_values
        if(len(pv) == 1):
            c = True

            row = single_values[x].row
            column = single_values[x].column
            square = single_values[x].square

            single_values[x].final_value = int(pv[0])
            single_values[x].possible_values = []

            row_values[row][x].final_value = pv[0]
            column_values[column][x].final_value = pv[0]
            square_values[square][x].final_value = pv[0]

            empty_values_indices.remove(x)


solution = "\nSolution:\n\n"
for x in single_values:
    if((x-1) % 9 == 0 and x != 1):
        solution += "||\n"
        if((x-1) % 27 == 0):
            solution += "-----------------------------------------\n"
        else:
            solution += "||           ||           ||           ||\n"
    if((x-1) % 3 == 0):
        solution += "|"
    
    add = "| " + str(single_values[x].final_value) + " "
    solution += add

    if(x == 81):
        solution += "||\n"

print(solution)

#0,0,5,0,0,0,9,0,7,0,4,7,1,0,0,0,0,0,0,2,0,0,0,4,8,0,0,0,0,0,0,0,0,6,0,0,2,0,0,0,9,0,0,0,5,0,0,3,4,0,0,0,0,2,4,0,0,0,8,0,0,0,0,3,0,2,0,0,0,0,0,6,0,7,9,0,0,2,5,0,0
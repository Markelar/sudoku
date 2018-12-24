from SingleValue import SingleValue

class Sudoku:

    input_values = {}
    single_values = {}

    def __init__(self, input_values):
        self.input_values = input_values
        
        triplet_counter = 1
        square_column_counter = 0
        square_row_counter = 0
        square_counter = -1
        c = 1

        for i in input_values:
            input_value = input_values[i]
            column = ((i-1) % 9) + 1 
            row = ((i-1) / 9) + 1

            if ((triplet_counter-1) % 3 == 0):
                triplet_counter = 1

                if (triplet_counter == 1):
                    square_column_counter += 1

                    if ((square_column_counter-1) % 3 == 0):
                        square_column_counter = 1
                        square_row_counter += 1

                        if((square_row_counter-1) % 3 == 0):
                            square_row_counter = 1
                            square_counter += 1

            square = square_column_counter + square_counter*3

            single_value = SingleValue(input_value, row, column, square)
            self.single_values[c] = single_value
            c += 1

            triplet_counter += 1

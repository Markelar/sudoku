class SingleValue:
    final_value = 0
    row = 0
    column = 0
    square = 0

    possible_values = []

    def __init__(self, final_value, row, column, square):
        self.final_value = final_value
        self.row = row
        self.column = column
        self.square = square
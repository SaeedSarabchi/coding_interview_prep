import copy
def zero_matrix(input_matrix):
    new_matrix = copy.deepcopy(input_matrix)

    for row_index in range(len(input_matrix)):
        for column_index in range(len(input_matrix[0])):
            if input_matrix[row_index][column_index] == 0:
                make_zero(new_matrix, row_index, column_index)
    return new_matrix


def make_zero(input_matrix, input_row_index, input_column_index):
    for row_index in range(len(input_matrix)):
        input_matrix[row_index][input_column_index] = 0
    for col_index in range(len(input_matrix[0])):
        input_matrix[input_row_index][col_index] = 0

print(zero_matrix([[1, 2, 0],[4, 5, 6]]))


#In-place:
def zero_matrix2(input_matrix):
    zero_rows = set()
    zero_columns = set()
    for row_index in range(len(input_matrix)):
        for column_index in range(len(input_matrix[0])):
            if input_matrix[row_index][column_index] == 0:
                zero_rows.add(row_index)
                zero_columns.add(column_index)
    in_place_zero(input_matrix, zero_rows, zero_columns)
    return input_matrix


def in_place_zero(input_matrix, zero_rows, zero_columns):
    for row_index in zero_rows:
        for column_index in range(len(input_matrix[0])):
            input_matrix[row_index][column_index] = 0

    for column_index in zero_columns:
        for row_index in range(len(input_matrix)):
            input_matrix[row_index][column_index] = 0

print(zero_matrix2([[1, 2, 0],[4, 5, 6]]))

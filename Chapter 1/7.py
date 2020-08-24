import math
def rotate_90(matrix):
    #new_matrix=[[None for i in range(len(matrix))] for j in range(len(matrix))]
    for i in range(math.ceil((len(matrix[0])/2))):
        for j in range(i, len(matrix[0])-i-1):

            temp = matrix[i][j]

            row_index = i
            column_index = j
            #left to top
            matrix[row_index][column_index] = matrix[len(matrix[0])-column_index-1][row_index]

            new_i = len(matrix[0])-column_index-1
            new_j = row_index
            # bottom to left
            matrix[new_i][new_j] = matrix[len(matrix[0]) - new_j - 1][new_i]

            row_index = len(matrix[0]) - new_j - 1
            column_index =  new_i
            matrix[row_index][column_index] = matrix[len(matrix[0]) - column_index - 1][row_index]

            new_i = len(matrix[0]) - column_index - 1
            new_j = row_index
            matrix[new_i][new_j] = temp



    return matrix


print(rotate_90([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

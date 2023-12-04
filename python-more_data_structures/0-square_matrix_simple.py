def square_matrix_simple(matrix=[]):
    new_matrix=[]
    for row in matrix:
        squared_row = []
        for col in row:
            col = col**2
            squared_row.append(col)
            
        new_matrix.append(squared_row)
    return new_matrix




def isToeplitzMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for i in range(width):
        for j in range(1,height):
            if i + j >= width:
                break
            else:
                if matrix[j][i+j] != matrix[0][i]:
                    return False
    for j in range(1,height):
        for i in range(width):
            if i+j >= height:
                break
            else:
                if matrix[i+j][i] != matrix[j][0]:
                    return False
    return True

# Sample Inputs:

# Expect True
isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])

# Expect False
isToeplitzMatrix([[1,2],[2,2]])
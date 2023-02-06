# GOAL:
# take input of an mxn augmented matrix
# print out that matrix in row echelon form
# bonus feature that shows the steps to get there

# Matrix will be stored in an mxn array
# The three operations used to convert to REF will be:
# 1) switch two rows
# 2) add two rows
# 3) scalar multiply a row

# input is the matrix (mxn array) and the two rows to switch (both ints)
# output is the new matrix with switched rows (mxn array)
def switch(matrix, row1, row2):
    newMatrix = []

    for row in range(len(matrix)):
        if row != row1 and row != row2:
            newMatrix.append(matrix[row])

        elif row == row1:
            newMatrix.append(matrix[row2])

        else:
            newMatrix.append(matrix[row1])

    return newMatrix


# input is the matrix (mxn array), the two rows to add, and the row to replace at the end (all ints)
# output is the new matrix (mxn array)
def add(matrix, row1, row2, replaceRow):
    newMatrix = []

    # create the sum of the two rows
    sumRow = []
    for index in range(len(matrix[row1])):
        sumRow.append(matrix[row1][index] + matrix[row2][index])

    # add everything back into the newMatrix
    for row in range(len(matrix)):
        if row != replaceRow:
            newMatrix.append(matrix[row])

        else:
            newMatrix.append(sumRow)

    return newMatrix

# input is the matrix (mxn array), the row to multiply, and the scalar to multiply by (all ints)
# output is the new matrix (mxn array) with the row to multiply replaced by the scalar multiple of that row
def multiply(matrix, multiplyRow, scalar):
    newMatrix = []

    multiple = []
    for index in range(len(matrix[multiplyRow])):
        multiple.append(matrix[multiplyRow][index] * scalar)

    for row in range(len(matrix)):
        if row != multiplyRow:
            newMatrix.append(matrix[row])

        else:
            newMatrix.append(multiple)

    return newMatrix

# Function to take in input for a matrix
# returns the matrix as an mxn array
def input():
    sizeStr = input("What are the dimensions of the matrix? (answer in the form mxn) ")
    rows = int(sizeStr[0])
    



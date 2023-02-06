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

# Utility funciton to copy a list without poitner errors >:(
def copyList(list):
    newList = []
    for item in list:
        newList.append(item)

    return newList

# Function to take in input for a matrix
# returns the matrix as an mxn array
def userInput():
    sizeStr = input("What are the dimensions of the matrix? (answer in the form mxn) ")
    rows = int(sizeStr[0:sizeStr.index('x')])

    print()

    matrix = []

    for row in range(rows):
        rowStr = input("Input the numbers in your row with spaces in between:\n")
        newRow = []

        currentNum = ""
        for character in rowStr:
            if character == ' ':
                newRow.append(int(currentNum))
                currentNum = ""
            else:
                currentNum += character

        # add in the last character
        if currentNum != "":
            newRow.append(int(currentNum))

        matrix.append(copyList(newRow))

    return matrix

# utility function to print the matrix
def printMatrix(matrix):
    print()
    for row in matrix:
        for num in range(len(row)):
            if num == len(row)-2:
                print(row[num], end = " | ")
            else:
                print(row[num], end = " ")
        print()
    print()


# OK algorithm time
# We're going to repeat this process for every column (except the last one)

# 2 cases:
# 1) We can make the top left potential leading one a leading one through scalar multiplication a
# - multiply that row by 1/(target number) to make the target number 1
# - then use scalar multiplication + addition to make every other number in that column a zero

# 2) We cannot make the top left potential leading one a leading one (i.e. everything in that column is a 0 except for rows that already have a leading 1)
# - move on to the next column

def REF(matrix):

    columnCount = len(matrix[0])-1
    lockedRows = 0

    for column in range(columnCount):
        firstNonZero = -1
        # find the first nonzero number in that column
        for row in range(len(matrix)):
            if matrix[row][column] != 0 and firstNonZero == -1 and row >= lockedRows:
                firstNonZero = row

        # check if any were found
        if firstNonZero != -1:
            matrix = switch(matrix, lockedRows, firstNonZero)

            matrix = multiply(matrix, lockedRows, 1/matrix[lockedRows][column])

            for row in range(len(matrix)):

                if matrix[row][column] != 0 and row != lockedRows:

                    multiplyNum = -matrix[row][column]

                    matrix = multiply(matrix, lockedRows, multiplyNum)

                    matrix = add(matrix, lockedRows, row, row)

                    matrix = multiply(matrix, lockedRows, 1/multiplyNum)

            lockedRows += 1

    return matrix

matrix0 = [[0, 0, -2, 0, 7, 12], [2, 4, -10, 6, 12, 28], [2, 4, -5, 6, -5, -1]]
matrix1 = [[1, 1, 2, 8], [-1, -2, 3, 1], [3, -7, 4, 10]]
matrix2 = [[2, -3, -2], [2, 1, 1], [3, 2, 1]]
matrix3 = [[5, -2, 6, 0], [-2, 1, 3, 1]]
matrix4 = [[1, 2, -4, 1], [2, 3, 8, 0], [-1, 9, 10, 5]]
printMatrix(REF(matrix4))

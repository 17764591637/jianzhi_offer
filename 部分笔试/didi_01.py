import numpy as np
 
def s_location(matrix):#定位S在矩阵中位置
    for i in range(len(matrix)):
        if 'S' in matrix[i]:
            j = matrix[i].index('S')
            return [i, j]
 
def findanother_S(matrix, i, j):#在大矩阵中沿可通过路径寻找其它S，若找到则说明是连通的
    if i<0 or i>=len(matrix) or j<0 or j>= len(matrix) or matrix[i][j] == '#':
        return False
    if matrix[i][j] == 'S':
        return True
    if findanother_S(matrix, i + 1, j):
        print(i+1, j)
        return True
    if findanother_S(matrix, i - 1, j):
        print(i-1, j)
        return True
    if findanother_S(matrix, i, j + 1):
        print(i, j+1)
        return True
    if findanother_S(matrix, i, j - 1):
        print(i, j-1)
        return True
    return False
 
def isok(matrix):#判断matrix矩阵中S是否可以到达无穷多位置
    i, j = s_location(matrix)  # i,j
 
    matrix = np.array(matrix)#把matrix变成每行、每列各3个（共九个）matrix的大矩阵
    matrix = np.concatenate([matrix] * 3, axis=1)
    matrix = np.concatenate([matrix] * 3, axis=0)
    matrix[i][j] = '#'
    print(matrix)
 
    if findanother_S(matrix, i + 1, j):
        print(i+1,j)
        return True
    if findanother_S(matrix, i - 1, j):
        print(i-1,j)
        return True
    if findanother_S(matrix, i, j + 1):
        print(i,j+1)
        return True
    if findanother_S(matrix, i, j - 1):
        print(i,j-1)
        return True
    print(i,j)
    return False
 
if __name__== '__main__':
    matrix1 = [['S', '#'], ['#', '.']]
    matrix2 = [['.', '.', '.'], ['#', '#', '#'], ['#', 'S', '#']]
    result = isok(matrix2)
    print(result)
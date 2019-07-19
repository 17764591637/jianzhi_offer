'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
把矩阵分为一个圈一个圈去运算
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for j in matrix[::-1]:
                    res.append(j.pop(0))
        return res

s = Solution()
res = s.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(res)
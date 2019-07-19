class Solution:
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if target in i:

                return True
        return False

s = Solution()
res = s.searchMatrix(matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]],target = 3)
print(res)
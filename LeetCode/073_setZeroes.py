'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的
所有元素都设为 0。请使用原地算法。
示例 1:
输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''
class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        r = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.append([i,j])
       # print(r)      
        for i in r:
            matrix[i[0]] = [0 for _ in range(n)]
        for i in r:
            for j in range(m):
                matrix[j][i[1]] = 0
        
        return matrix

s = Solution()
res = s.setZeroes([
    [1,1,1],
    [1,0,1],
    [1,1,1]
  ])
print(res)
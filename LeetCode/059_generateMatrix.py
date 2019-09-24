'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n):
        array = [[0 for i in range(n)] for j in range(n)]
        c,j = 1,0
        while c<=n*n:
            #从左到右
            for i in range(j,n-j):
                array[j][i] = c
                c += 1
            #从上往下
            for i in range(j+1,n-j):
                array[i][n-j-1] = c
                c += 1
            #从右往左
            for i in range(n-j-2,j-1,-1):
                array[n-j-1][i] = c
                c += 1
            #从下往上
            for i in range(n-j-2,j,-1):
                array[i][j] = c 
                c += 1
            j += 1
        
        return array
 
s = Solution()
res = s.generateMatrix(3)
print(res)

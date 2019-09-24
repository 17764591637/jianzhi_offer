'''
给定一个包含m x n个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，
返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix and matrix[0]:
            first = matrix.pop(0)
            res += first
            for i in matrix:
                res += [i.pop()]
            if matrix:
                second = matrix.pop()
                res += second[::-1]
            if matrix:
                for j in matrix[::-1]:
                    if j != []:
                        res += [j.pop(0)]
        return res

s = Solution()
res = s.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(res)



        
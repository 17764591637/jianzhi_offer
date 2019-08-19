'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]]
            while len(res) != numRows:
                tmp = [1]
                for i in range(len(res[-1])-1):
                    tmp.append(res[-1][i] + res[-1][i+1])
                tmp.append(1)
                res.append(tmp)
                if len(res) == numRows:
                    break
            return res

s = Solution()
res = s.generate(5)
print(res)
        
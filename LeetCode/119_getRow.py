'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
示例:

输入: 3
输出: [1,3,3,1]
'''
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            res = [[1],[1,1]]
            while len(res) != rowIndex+1:
                tmp = [1]
                for i in range(len(res[-1])-1):
                    tmp.append(res[-1][i] + res[-1][i+1])
                tmp.append(1)
                res.append(tmp)
            return res[-1]

            
s = Solution()
res = s.getRow(2)
print(res)
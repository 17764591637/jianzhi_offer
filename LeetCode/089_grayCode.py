'''
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
思路：已知n-1的格雷码集合，在前面加一个0，
然后把n-1的集合倒转在前面加一个1，就得到n的格雷码集合
'''
class Solution:
    def grayCode(self, n):
        flag = {'0':1,'1':-1}
        if n == 0:
            return [0]
        def dfs(n):
            if n == 1:
                return ['0','1']
            res = []
            for i in ['0','1']:
                tmp = dfs(n-1)
                for j in tmp[::flag[i]]:
                    res.append(i+j)
            return res
        r = []
        for i in dfs(n):
            #print(i)
            r.append(int(i,2))

        return r

s = Solution()
res = s.grayCode(2)
print(res)
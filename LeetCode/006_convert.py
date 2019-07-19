class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 思路：找规律，将每层的数值单独存储，最后合并
        if numRows == 1 or s == '':
            return s
        d = {}
        for i in range(numRows):
            d[i] = ''
        space = 2*numRows - 2           # 第一行每个元素的间隔
        for i, item in enumerate(s):
            if i//(numRows-1)%2 == 0:
                d[i%space] += item
            else:
                d[space-i%space] += item

        # 合并从上到下的层
        res = ''
        for i in range(numRows):
            res += d[i]
        return res

s = Solution()
res = s.convert('LEETCODEISHIRING',3)
print(res)
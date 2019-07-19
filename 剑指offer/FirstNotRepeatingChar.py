'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个
只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        str_set = set(s)
        res = []
        for i in str_set:
            if s.count(i) == 1:
                res.append(i)
        if not res:
            return -1
        for j in s:
            if j in res:
                return s.index(j)

s = Solution()
res = s.FirstNotRepeatingChar('kkll')
print(res)
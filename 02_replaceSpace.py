'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = ''
        for i in s:
            if i != ' ':
                res += i
            else:
                res += '%20'

        return res 
s = Solution()
res = s.replaceSpace('We Are Happy')
print(res)
'''
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        res = ''
        str_1 = s[0:n]
        str_2 = s[n:]
        res = str_2 + str_1

        return res


s = Solution()
res = s.LeftRotateString('qereggdh',6)
print(res)
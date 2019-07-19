'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。
'''
class Solution:
    def StrToInt(self, s):
        # write code here
        try:
            s_int = int(s)
        except:
            return 0

        return int(s)


s = Solution()
res = s.StrToInt('asd')
print(res)

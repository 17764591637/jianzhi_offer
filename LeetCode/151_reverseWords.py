'''
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

'''
class Solution:
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        res = ' '.join(s)
        
        return res

s = Solution()
res = s.reverseWords("the sky is   blue!")
print(res)
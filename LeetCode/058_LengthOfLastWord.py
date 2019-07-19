'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Input: "Hello World"
Output: 5
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.strip().split(' ')
        if s_list[-1].isalpha() == False:
            return 0
        return len(s_list[-1])
a = Solution()
l = a.lengthOfLastWord("a ")
print(l)

'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
最长的回文子串。

中心扩散：选取一个中心点向两边扩散并判断是否为回文，并记录所有搜索到的最长回文并返回结果。
'''
class Solution(object):

    def longestPalindrome(self, s):
        start = end = 0
        for i in range(len(s)):
            len1 = self.centerexpand(s,i,i)
            len2 = self.centerexpand(s,i,i+1)

            maxlen = max(len1,len2)

            if maxlen > end - start + 1:
                start = i - (maxlen-1)//2
                end = i + maxlen//2

        return s[start:end+1]


    def centerexpand(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1#计算到l=-1
            r += 1

        return r-l-1

s = Solution()
str = s.longestPalindrome('bab')
print(str)
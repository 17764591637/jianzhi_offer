"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in str.
Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
思路：
直接 one line 的思路：
转换成列表，然后一致。判断下字符位数的不同。
同样的思路换成这个题就能跑20ms..
beat 99%.
"""
class Solution(object):
    def wordPattern(self, pattern, string):
        str_list = string.split()
        pattern = list(pattern)
        if len(str_list) != len(pattern):
            return False
        #print(list(zip(pattern,str_list)))
        s = set(zip(pattern,str_list))
        return len(s) == len(set(pattern)) == len(set(str_list))
s =Solution()
print(s.wordPattern(pattern = "egg", string = "a d d"))
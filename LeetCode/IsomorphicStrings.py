"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
给定两个字符串，判断是否属于相同的模式。
这个没想到什么好办法，就是根据字典进行替换然后对比是否一致。
先上自己的思路：
迭代字符串a，如果遇到的是a_d中的字符串，则根据a_d替换，否则将其根据出现的顺序添加到a_d中，
这样做让每个单词根据字符所出现的顺序进行字典替换。
测试用例：
https://leetcode.com/problems/isomorphic-strings/description/
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_k = 0
        t_k = 0
        s_d = {}
        t_d = {}
        new_s = ''
        new_t = ''
        for i in s:
            if s_d.get(i):
                new_s += s_d.get(i)
            else:
                s_d[i] = str(s_k)
                s_k += 1

        for i in t:
            if t_d.get(i):
                new_t += t_d.get(i)
            else:
                t_d[i] = str(t_k)
                t_k += 1
        print(new_s)
        return new_s == new_t

s = 'paper'
t = 'title'
a = Solution()
a.isIsomorphic(s,t)
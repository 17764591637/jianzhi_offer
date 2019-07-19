"""
Count the number of segments in a string, where a segment is defined to
be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5
就是根据空白分割，然后统计数量，没什么难度。O(n).
Python中可以直接 len(s.split()).
测试用例：
https://leetcode.com/problems/number-of-segments-in-a-string/description/
"""
class Solution(object):
    def countSegments(self, s):
        if not s.strip():
            return 0
        s = s.strip().split(' ')
        res = []
        for i in s:
            if len(i) != 0:
                res.append(i)
        return len(res)

s = Solution()
ss = s.countSegments(", , , ,        a, eaefa")
print(ss)

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s):
        res = []
        def backtrack(List, tmp):
            if not List:
                res.append(tmp)
                return
            for i in range(len(List)):
                if List[:i+1] == List[i::-1]:
                    backtrack(List[i+1:], tmp + [List[:i+1]])

        backtrack(s,[])
        return res

s = Solution()
res = s.partition('aab')
print(res)
        
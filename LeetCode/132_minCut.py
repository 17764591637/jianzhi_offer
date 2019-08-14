'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回符合要求的最少分割次数。
示例:
输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
'''
# class Solution:
#     def minCut(self, s):
#         res = []
#         def backtrack(List, tmp):
#             count = float('inf')
#             if not List:
#                 if len(tmp)-1 <= count:
#                     count = len(tmp)-1
#                     res.append(count)
#                 return 
#             for i in range(len(List)):
#                 if List[:i+1] == List[i::-1]:
#                     backtrack(List[i+1:], tmp + [List[:i+1]])

#         backtrack(s,[])

#         return min(res)

class Solution:
    def minCut(self, s):
        dp = [len(s) for i in range(len(s)+1)]
        print(dp)
        dp[0] = -1 
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i+1] = min(dp[i+1],dp[j]+1)

        return dp[-1]

s  = Solution()
res = s.minCut('aab')
print(res) 
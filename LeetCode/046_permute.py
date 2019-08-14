# class Solution:
#     def permute(self, nums):
#         res = []
#         def backtrack(nums,tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i+1:], tmp+[nums[i]])

#         backtrack(nums,[])
#         return res

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(num, path):
            if not num:
                res.append(path)
                return
            for i in range(len(num)):
                dfs(num[:i]+num[i+1:], path+[num[i]])
        dfs(nums, [])
        return res 
    
s = Solution()
res = s.permute([1,2,3])
print(res)
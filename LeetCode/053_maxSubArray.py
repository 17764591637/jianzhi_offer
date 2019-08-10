# class Solution:
#     def maxSubArray(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         curr = 0
#         res = nums[0]
#         for i in nums:
#             curr = curr + i
#             if curr > res:
#                 res = curr
#             if curr < 0:
#                 curr = 0
#         return res

class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0 
        d = []
        d.append(nums[0])
        max_ = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i] + d[i-1]:
                d.append(nums[i])
            else:
                d.append(nums[i]+d[i-1])
            if max_ < d[i]:
                max_ = d[i]

        return max_

s = Solution()
res = s.maxSubArray([-2,-3])
print(res)

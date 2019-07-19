class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        curr = 0
        res = nums[0]
        for i in nums:
            curr = curr + i
            if curr > res:
                res = curr
            if curr < 0:
                curr = 0
        return res


s = Solution()
res = s.maxSubArray([-2,-3])
print(res)

class Solution:
    def majorityElement(self, nums):
        res = []
        s = set(nums)
        for i in s:
            num_count = nums.count(i)
            if num_count>len(nums)/2:
                if i not in res:
                    return i 

s = Solution()
res = s.majorityElement([3,2,3])
print(res)
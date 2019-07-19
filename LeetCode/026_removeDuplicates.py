class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        curr = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[curr]:
                curr += 1
                nums[curr] = nums[i]

        return curr+1

s = Solution()
res = s.removeDuplicates(nums = [1,1,2])
print(res)

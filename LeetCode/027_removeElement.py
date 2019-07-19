class Solution:
    def removeElement(self, nums, val):
        '''if len(nums) == 0:
            return len(nums)
        if len(nums) == 1 and nums[0] == val:
            return 0'''

        curr = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        print(nums)

        return curr

s = Solution()
res = s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(res)
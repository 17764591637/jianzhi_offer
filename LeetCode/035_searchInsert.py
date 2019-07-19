class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            res = nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            res = nums.index(target)

        return res


s = Solution()
res = s.searchInsert([1,3,5,6], 2)
print(res)

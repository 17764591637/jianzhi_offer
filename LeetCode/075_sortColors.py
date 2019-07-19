class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        while not self.fun(nums):
            for i in range(len(nums)-1):
                if nums[i+1] <= nums[i]:
                    a = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = a
        print(nums)

    def fun(self,nums):
        if len(nums) == 1:
            return True
        else:
            for i in range(len(nums)-1):
                if i == len(nums)-2 and nums[i+1] >= nums[i]:
                    return True
                elif nums[i+1] >= nums[i] and i != len(nums)-2:
                    continue
                else:
                    return False

class Solution(object):
    def sortColors(self,nums):
        l_point = -1
        r_point = len(nums)
        i = 0
        while i < len(nums) and i < r_point:
            if nums[i] == 0 and i > l_point:
                l_point += 1
                nums[l_point],nums[i] = nums[i],nums[l_point]
            elif nums[i] == 2:
                r_point -= 1
                nums[r_point],nums[i] = nums[i],nums[r_point]

            else:
                i += 1
        return nums
s = Solution()
res = s.sortColors([2,0,2,1,1,0])
#print(res)
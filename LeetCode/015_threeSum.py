class Solution:
    def threeSum(self, nums):
        nums.sort()#先对数组排序
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res

s = Solution()
res = s.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
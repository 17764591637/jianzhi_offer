class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # 先对数组排序
        res = 0
        mindiff = float('inf')
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = s-target
                #print(diff)
                if abs(diff) < mindiff:
                    res = (nums[i]+nums[l]+nums[r])
                    mindiff = min(mindiff,abs(diff))
                if s-target == 0:
                    res = (nums[i]+nums[l]+nums[r])
                elif s-target < 0:
                    l += 1
                else:
                    r -= 1
        return res

s = Solution()
res = s.threeSumClosest([0,1,2],3)
print(res)
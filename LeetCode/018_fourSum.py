class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # 先对数组排序
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r] + nums[j]
                    if target-s == 0:
                        ans = [nums[i], nums[l], nums[r],nums[j]]
                        if ans not in res:
                            res.append(ans)
                        l += 1
                        r -= 1
                    elif s-target < 0:
                        l += 1
                    else:
                        r -= 1
        return res

s = Solution()
res = s.fourSum(nums = [1,0,-1,0,-2,2],target = 0)
print(res)
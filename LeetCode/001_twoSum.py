class Solution(object):
  def twoSum(self, nums, target):
      res = []
      for x,y in enumerate(nums):
          if target-y in nums:
              if nums.index(target-y) != x:
                res.append(x)
                index = nums.index(target-y)
                res.append(index)

      return list(set(res))

s =Solution()
res = s.twoSum(nums = [3,2,4], target = 6)
print(res)
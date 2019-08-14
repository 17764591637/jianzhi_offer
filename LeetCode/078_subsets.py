'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums):
        res = [[],nums]
        for ii in range(1,len(nums)):
            def backtrack(i, tmp):
                if len(tmp) == ii:
                    if len(set(tmp)) != ii:
                        return
                    res.append(tmp)
                    return
                for j in range(i,len(nums)):
                    backtrack(j + 1, tmp + [nums[j]])

            backtrack(0, [])
        return res

s = Solution()
res = s.subsets(['a','a','b'])
print(res)
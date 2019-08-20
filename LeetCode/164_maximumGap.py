'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
'''
class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            res = 0
            for i in range(len(nums)-1):
                gap = nums[i+1] - nums[i]
                if gap >= res:
                    res = gap 
            return res 

s = Solution()
res = s.maximumGap([1,1,1,1,1,5,5,5,5,5])
print(res)
        
        
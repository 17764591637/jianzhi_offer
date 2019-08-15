'''
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。
如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
'''
# class Solution:
#     def containsDuplicate(self, nums):
#         nums.sort()
#         for i in range(1,len(nums)):
#             if nums[i-1] == nums[i]:
#                 return True
#         return False

class Solution:
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return True
        
        return False
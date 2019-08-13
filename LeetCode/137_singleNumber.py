'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
'''
# class Solution:
#     def singleNumber(self, nums):
#         for i in nums:
#             if nums.count(i) == 1:
#                 return i

# class Solution:
#     def singleNumber(self, nums):
#         a, b = 0, 0
#         for num in nums:
#             b = ~a & (b ^ num)
#             a = ~b & (a ^ num)
#         return b

class Solution:
    def singleNumber(self, nums):
        return int((3*sum(set(nums))-sum(nums))/2)
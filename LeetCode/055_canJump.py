'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
思路：
从后往前遍历数组，如果遇到的元素可以到达最后一行，则截断后边的元素。
否则继续往前，若最后剩下的元素大于1个，则可以判断为假。否则就是真，时间复杂度O(n)。
'''
class Solution:
    def canJump(self, nums):
        #方法一
        # n = 1
        # for i in range(len(nums)-2,-1,-1):
        #     if nums[i] >= n:
        #         n = 1
        #     else:
        #         n += 1
        #     if i == 0 and n > 1:
        #         return False
        # return True

        #方法二
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < len(nums) - 1:
            end = max(end,nums[start] + start)  
            start += 1
        return end>=n-1 

s = Solution()
res = s.canJump(
[2,3,1,1,4])
print(res)
'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列
（该序列至少包含一个数）。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

动态规划，使用dp_min和dp_max分别保存到i为止连续子序列乘积的最大值和最小值
'''
class Solution:
    def maxProduct(self, nums):
        max_list = [0 for _ in range(len(nums))]
        min_list = [0 for _ in range(len(nums))]
        max_list[0] = nums[0]
        min_list[0] = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            max_list[i] = max(max_list[i - 1] * nums[i], max(min_list[i - 1] * nums[i], nums[i]))
            min_list[i] = min(max_list[i - 1] * nums[i], min(min_list[i - 1] * nums[i], nums[i]))
            res = max(res, max_list[i])
        return res
s = Solution()
res = s.maxProduct([-2,3,-4])
print(res)
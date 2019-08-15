'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同
的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 
的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true

'''
# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         count_2 = []
#         for i in range(len(nums)):
#             if nums.count(nums[i]) > 1:
#                 count_2.append(nums[i])
#         count_2 = set(count_2)
#         max_len = 0
#         for num in count_2:
#             tmp = [i for (i,j) in enumerate(nums) if j == num]
#             print(tmp)
#             if tmp[-1] - tmp[0] > max_len:
#                 max_len = tmp[-1] - tmp[0]
#         if max_len == k:
#             return True
#         return False
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        nums_len = len(nums)
        if nums_len <= 1:
            return False
        nums_dict = {}
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if i - nums_dict[nums[i]] <= k:
                    return True
            
            nums_dict[nums[i]] = i
        return False
s = Solution()
res = s.containsNearbyDuplicate([1,0,1,1],1)
print(res)
        
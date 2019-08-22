'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

翻转：
arr = [1,2,3,4,5] --右移两位--> [4,5,1,2,3] 
假设 n = arr.length，k = 右移位数，可得：  
     [1,2,3,4,5] --翻转索引为[0,n-1]之间的元素--> [5,4,3,2,1] 
                 --翻转索引为[0,k-1]之间的元素--> [4,5,3,2,1] 
                 --翻转索引为[k,n-1]之间的元素--> [4,5,1,2,3]
'''
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        if len(nums) == 0 or k == 0:
            return
        def reverse(start,end,s):
            while start < end:
                s[start],s[end] = s[end],s[start]
                start += 1 
                end -= 1
        n = len(nums) - 1
        k = k % len(nums)
        reverse(0,n-k,nums)
        reverse(n-k+1,n,nums)
        reverse(0,n,nums) 
        
s = Solution()
res = s.rotate([1,2,3,4,5,6,7],3) 
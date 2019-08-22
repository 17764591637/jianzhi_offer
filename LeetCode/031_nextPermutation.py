'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #第一步，从后往前，找到下降点
        down_index = None
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                down_index = i 
                break
        #print(down_index)
        if down_index is None:
            nums.reverse()
        else:
            #第二步，从后往前，找到比下降点大的数，对换位置
            for i in range(len(nums)-1,i,-1):
                if nums[down_index] < nums[i]:
                    nums[down_index],nums[i] = nums[i],nums[down_index]  
                    break
            #第三步，重新排列下降点之后的数
            #print(nums)
            i,j = down_index+1,len(nums)-1
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1

s = Solution()
res = s.nextPermutation([3,5,1,4,3,2])

        
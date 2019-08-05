'''
输入一个包含n个整数数组，按从左往右的顺序选出尽量多的整数，组成一个上升子序列，
要求输出最长上升子序列的长度。例如，输入序列1,6,2,3,7,5，最长上升子序列为1,2,3,5，
因此输出长度为4.要求：选出的上升子序列中相邻元素不能相等。
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        a=[]
        if len(nums)==0:
            return 0
        a.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>a[-1]:
                a.append(nums[i])
            else:
                if nums[i]<a[0]:
                    a[0]=nums[i]
                else:
                    position=self.binarySearch(a,nums[i],0,len(a)-1)
                    a[position]=nums[i]
        return len(a)
            
    def binarySearch(self,a,number,left,right):
        if left==right:
            return left
        while left<right:
            mid=(left+right)//2
            if mid==left or mid==right:
                if number>a[left]:
                    return right
                else:
                    return left
            if number<a[mid]:
                return self.binarySearch(a,number,left,mid)
            else:
                return self.binarySearch(a,number,mid,right)

solut = Solution()
print(solut.lengthOfLIS([1,6,2,3,7,5]))

# def lengthOfLIS(self, nums):
#     tails = [0] * len(nums)
#     size = 0
#     for x in nums:
#         i, j = 0, size
#         while i != j:
#             m = (i + j) // 2
#             if tails[m] < x:
#                 i = m + 1
#             else:
#                 j = m
#         tails[i] = x
#         size = max(i + 1, size)
#     return size


# if '__name__ = __main__':
#     a = [2, 7, 1, 5, 6, 4, 3, 8, 9]
#     count = lengthOfLIS(a)
#     print(count)



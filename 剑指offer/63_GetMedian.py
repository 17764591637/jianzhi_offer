'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''
class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        # write code here
        self.nums.append(num)

        return self.nums

    def GetMedian(self,nums):
        # write code here
        nums = self.nums
        nums.sort()
        n = len(nums)//2
        if len(nums)%2 != 0:
            
            return nums[n]
        else:
            
            return (nums[n]+nums[n-1])/2.0

s = Solution()
s.Insert(1)
s.Insert(2)
s.Insert(4)
s.Insert(6)
s.Insert(3)
res = s.GetMedian([1,2,4,6,3])
print(res)
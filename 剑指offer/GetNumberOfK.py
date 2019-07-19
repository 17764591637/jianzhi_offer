'''
统计一个数字在排序数组中出现的次数。
'''
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0 
        count = data.count(k)
        
        return count

s = Solution()
res = s.GetNumberOfK([1,2,3,4,5,6,7,0],3)
print(res)
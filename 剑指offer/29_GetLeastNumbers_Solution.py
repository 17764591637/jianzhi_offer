'''
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        else:
            tinput.sort()

            return tinput[0:k]



s = Solution()
res = s.GetLeastNumbers_Solution([1,2,3,2,2,2,5,4,2],4)
print(res)
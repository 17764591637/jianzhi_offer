'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：
寻找规律
2**（n-1）
'''
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        else:
            return 2**(number-1)

s = Solution()
res = s.jumpFloorII(5)
print(res)
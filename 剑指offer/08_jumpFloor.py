'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
class Solution:
    def jumpFloor(self, number):
        r = [1,2]
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            for i in range(number-2):
                res = r[-1]+r[-2]
                r.append(res)
            
            return res

s = Solution()
res = s.jumpFloor(4)
print(res)
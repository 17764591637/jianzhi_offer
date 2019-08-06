'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
寻找规律
res = r[-1]+r[-2]
'''
class Solution:
    def rectCover(self, number):
        # write code here
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
res = s.rectCover(4)
print(res)
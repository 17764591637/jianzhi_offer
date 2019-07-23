'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
如果n大于0，直接计算即可，如果n小于0，计算2的32次方加上n的结果中1的个数
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0 :
            num_bin = bin(n)
            res = num_bin.count('1')

            return res
        else:
            n += 2**32
            num_bin = bin(n)
            res = num_bin.count('1')

            return res

s = Solution()
res = s.NumberOf1(-1)
print(res)
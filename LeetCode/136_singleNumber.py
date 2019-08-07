'''
根据异或的运算法则，2^2^3^1^1=0^3^0=3
'''
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
           res ^= i
        
        return res
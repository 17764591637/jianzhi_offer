'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330
'''
class Solution:
    def largestNumber(self, nums):
        length = len(nums)
        i = length
        while i > 0:
            for j in range(i-1):
                a = nums[j]
                b = nums[j+1]
                ab = int(str(a) + str(b))
                ba = int(str(b) + str(a))
                if ba > ab:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                print(nums)
            i -= 1
        
        res = ''
        for n in nums:
            if res == '' and n == 0:
                continue
            res += str(n)
        if res == '':
            return 0
        else:
            return res

        return res

s  = Solution()
res = s.largestNumber([3,30,34,5,9])
print(res)
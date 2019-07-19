'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        r = float('inf')
        res = []
        a = 0
        for i in array:
            if tsum-i in array:
                res.append([i,tsum-i])
        if len(res) == 1:
            return res
        elif res == []:
            return []
        else:
            for j in range(len(res)):
                s = res[j][0]*res[j][1]
                if s <= r:
                    r = s 
                    a = j
            res = sorted(res[a])
            return res
            
s = Solution()
res = s.FindNumbersWithSum([1,2,3,4,5,7,11,15],6)
print(res)
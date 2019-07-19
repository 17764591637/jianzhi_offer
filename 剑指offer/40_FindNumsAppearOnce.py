'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        res = []
        s = set(array)
        for i in s:
            if array.count(i) == 1:
                res.append(i)
        
        return res

s = Solution()
res = s.FindNumsAppearOnce([1,2,1,2,3,4,5,5])
print(res)
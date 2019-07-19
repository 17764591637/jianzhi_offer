'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
class Solution:
    def Sum_Solution(self, n):
        # write code here
        num_list = [i for i in range(1,n+1)]
        return sum(num_list)


s = Solution()
res = s.Sum_Solution(6)
print(res)
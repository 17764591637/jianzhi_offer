'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            i = str(i)
            if '1' in i:
                count += i.count('1')

        return count


s = Solution()
res = s.NumberOf1Between1AndN_Solution(55)
print(res)
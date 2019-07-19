class Solution:
    def isHappy(self, n):
        while True:
            if self.fun(n) == 1:
                return True   
            else:
                n = self.fun(n)
                if n == 89:
                    return False     
        return False

    def fun(self, m):
        sum_ = 0
        n_str = str(m)
        for i in n_str:
            sum_ += int(i)**2 

        return sum_

s = Solution()
res = s.isHappy(1111111)
print(res)
        
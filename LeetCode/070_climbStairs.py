class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n > 1:
            r = self.func(n)
            return r[n-2]

    def func(self,n):
        r = [2,3]
        a = 2
        b = 3
        for i in range(3,n):
            sum = a + b
            r.append(sum)
            a = b
            b = sum

        return r

s = Solution()
res = s.climbStairs(4)
print(res)
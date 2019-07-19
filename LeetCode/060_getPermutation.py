'''class Solution(object):
    def getPermutation(self, n, k):
        nums = list(range(1,n+1))
        res = []
        def backtrack(nums ,tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[ i +1:], tmp + [str(nums[i])])
    
        backtrack(nums ,[])

        return ''.join(res[k-1])'''


'''class Solution:
    def getPermutation(self, n, k):
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        # 找到对应的n应该对应的fac坐标,就是在第一项确定的情况一下，有(n-1)!种组合
        i = n - 1
        # 构建序列，这个num是用来储存我们当前可以添加的数的，也是为避免重复
        num = list(range(1, n + 1))
        ret = ""
        while i >= 0:
            # a用来获得我们要求的那一位在num里的下标
            a, b = k // self.fac[i], k % self.fac[i]
            # 如果刚好整除干净，证明还在上一层
            if b == 0:
                a -= 1
            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            # 如果刚好整除完，则我们已经可以知道接下来的排序情况了，它一定是最大的
            # 所以把剩下的可选的数字reverse来制造这种效果
            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret
'''


class Solution:
    def getPermutation(self, n, k):
        series = [str(i + 1) for i in range(n)]
        res = ''
        cr = self.factorial(n)
        while n:
            cr //= n
            n -= 1
            temp = (k - 1) // cr
            res += series.pop(temp)
            k -= cr * temp
        return res

    def factorial(self, n):
        if n < 2:
            return 1
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

s = Solution()
res = s.getPermutation(n=3,k=3)
print(res)
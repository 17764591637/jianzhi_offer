class Solution:
    def combine(self, n, k):
        res = []
        nums = list(range(1,n+1))
        def backtrack(i,tmp):
            if len(tmp) == k:
                if len(set(tmp)) != k:
                    return
                res.append(tmp)
                return
            for j in range(i, n):
                backtrack(j+1,tmp+[nums[j]])

        backtrack(0,[])
        return res

s = Solution()
res = s.combine(3,3)
print(res)
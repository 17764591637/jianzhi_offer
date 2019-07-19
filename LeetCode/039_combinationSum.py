class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if  tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j,tmp_sum+candidates[j],tmp+[candidates[j]])
        backtrack(0, 0, [])
        return res

s = Solution()
res = s.combinationSum([2,3,6,7],7)
print(res)
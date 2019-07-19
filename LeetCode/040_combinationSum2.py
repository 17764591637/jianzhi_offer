class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                    print(j)
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backtrack(j+1,tmp_sum + candidates[j],tmp+[candidates[j]])
        backtrack(0, 0, [])
        return res

s = Solution()
res = s.combinationSum2(candidates=[1,1,2,3,4,5],target=4)
print(res)
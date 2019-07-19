class Solution:
    def subsetsWithDup(self, nums):
        res = [[], nums]
        for ii in range(1, len(nums)):
            def backtrack(i, tmp):
                if len(tmp) == ii:
                    tmp.sort()
                    if tmp not in res:
                        res.append(tmp)
                        return
                for j in range(i, len(nums)):
                    backtrack(j + 1, tmp + [nums[j]])

            backtrack(0, [])
        return res


s = Solution()
res = s.subsetsWithDup([4,4,4,1,4])
print(res)
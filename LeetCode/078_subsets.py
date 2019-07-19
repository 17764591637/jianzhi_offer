class Solution:
    def subsets(self, nums):
        res = [[],nums]
        for ii in range(1,len(nums)):
            def backtrack(i, tmp):
                if len(tmp) == ii:
                    if len(set(tmp)) != ii:
                        return
                    res.append(tmp)
                    return
                for j in range(i,len(nums)):
                    backtrack(j + 1, tmp + [nums[j]])

            backtrack(0, [])
        return res

s = Solution()
res = s.subsets([1,2,3,4])
print(res)
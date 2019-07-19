class Solution:
    def firstMissingPositive(self, nums):
        if 1 not in nums:
            res = 1
        else:
            i = 0
            while True:
                if i+1 in nums:
                    i += 1
                    continue
                else:
                    res = i+1
                    break

        return res


s = Solution()
res = s.firstMissingPositive([-2,-5,-7,1,2,0])
print(res)

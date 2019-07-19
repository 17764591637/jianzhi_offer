class Solution:
    def plusOne(self, digits):
        num = ''
        for i in digits:
            num += str(i)
        num = int(num)
        r = num+1
        res = []
        for i in str(r):
            res.append(int(i))

        return res

s = Solution()
res = s.plusOne([4,3,2,1])
print(res)
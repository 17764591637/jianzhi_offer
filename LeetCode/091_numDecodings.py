class Solution:
    def numDecodings(self, s):
        if len(s) == 1 or s[0] == "0":
            return 0 if s[0] == "0" else 1
        res = []
        res.append(1)
        res.append(1)

        for i in range(1, len(s)):
            temp1 = int(s[i-1:i+1])
            temp = (0 if int(s[i])==0 else res[-1]) + (0 if temp1 > 26 or temp1<10 else res[-2])

            res.append(temp)

        return res[len(s)]


s = Solution()
res = s.numDecodings('2125')
print(res)
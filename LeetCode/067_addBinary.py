class Solution:
    def addBinary(self, a, b):
        add = int(a,2) + int(b,2)

        return bin(add)[2:]


s = Solution()
res = s.addBinary(a = "11", b = "1")
print(res)
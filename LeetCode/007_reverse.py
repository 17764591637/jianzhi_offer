class Solution:
    def reverse(self, x: int) -> int:

        if x >= 0:
            x = list(str(x))
            x.reverse()

            res = int(''.join(x))
        else:
            x = list(str(x)[1:])
            x.reverse()

            res = int(''.join(x))*(-1)

        if res > 2147483647 or res < -2147483648:
            return 0
        else:
            return res





s = Solution()
res = s.reverse(-123)
print(res)

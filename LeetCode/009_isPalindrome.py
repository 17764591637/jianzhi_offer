class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        x_reverse = list(reversed(x))

        return x == x_reverse
s = Solution()
res = s.isPalindrome(3443)
print(res)

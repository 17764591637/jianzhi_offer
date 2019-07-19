class Solution:
    def romanToInt(self, s: str) -> int:
        t = []
        dic = {'M':1000, 'CM': 900, 'D': 500,'CD':400,'C': 100, 'XC': 90,
               'L': 50,'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I':1}
        for i in s[::-1]:
            t.append(dic[i])
        res = t[0]
        for i in range(len(t)-1):
            if t[i]>t[i+1]:
                res -= t[i+1]
            else:
                res += t[i+1]
        return res

s = Solution()
res = s.romanToInt('MCMXCIV')
print(res)
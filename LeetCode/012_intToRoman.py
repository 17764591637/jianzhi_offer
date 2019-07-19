class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',
               50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        while num > 0:
            for key in dic:
                if num - key >= 0:
                    res += dic[key]
                    num -= key
                    break
        return res

s = Solution()
res = s.intToRoman(3230)
print(res)
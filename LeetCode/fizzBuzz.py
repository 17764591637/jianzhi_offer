class Solution:
    def fizzBuzz(self, n):
        swich = {3:'Fizz',5:'Buzz'}
        res = []
        for i in range(1,n+1):
            if i not in swich and i%3 != 0 and i%5 !=0:
                res.append(str(i))
            elif i%3 == 0 and i%5 != 0:
                res.append(swich[3])
            elif i%5 == 0 and i%3 != 0:
                res.append(swich[5])
            elif i%3 == 0 and i%5 == 0:
                res.append(swich[3]+swich[5])
        return res
s = Solution()
res = s.fizzBuzz(15)
print(res)
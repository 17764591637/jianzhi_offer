'''
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39 '''
class Solution:
    def __init__(self):
        self.res = [0,1,1]

    def Fibonacci(self, n): 
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(n-2):
                self.res.append(self.res[-1]+self.res[-2])

            return self.res[-1]

s = Solution()
res = s.Fibonacci(3)
print(res)
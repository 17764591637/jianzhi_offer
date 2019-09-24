import sys 
sys.setrecursionlimit(10000)

class Solution:
    def cal(self,C,N,k):
        value_sum = 0 
        value_sum = value_sum + ((N-1)/N)**C
        for i in range(1,k+1):
            value_sum += self.gen_last_value(C,i)*(1/N)**i*((N-1)/N)**(C-i)
        res = 1 - value_sum
 
        return res

    def get_value(self,n):
        if n==1:
            return n
        else:
            return n * self.get_value(n-1)
        
    def gen_last_value(self,n,m):
        first = self.get_value(n)
        second = self.get_value(m)
        third = self.get_value((n-m))

        return first/(second * third)

s = Solution()
res = s.cal(C=1000,N=500,k=10)
print(res)

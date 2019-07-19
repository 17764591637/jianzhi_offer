'''
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? 
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        for i in range(1,int(tsum/2)+1):
            for j in range(i,int(tsum/2)+2):
                sum_ = (j+i)*(j-i+1)/2
                if sum_>tsum:
                    break
                elif sum_ == tsum:
                    res.append(list(range(i,j+1)))
             
        return res
        
s = Solution()
res = s.FindContinuousSequence(100)
print(res)
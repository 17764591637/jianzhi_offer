'''
问题描述
一个环上有10个点，编号为0-9，从0点出发，每步可以顺时针到下一个点，也可以逆时针到上一个点，求：经过n步又
回到0点有多少种不同的走法
思路(动态规划)
我们可以想到，再回到0点可以从右面回来，也可以从左面回来，即先到达旁边的一个点，看看有多少回来的方法
即可。所以运用动态规划的思想，我们可以写出递推式如下：
d(k, j) = d(k-1, j-1) + d(k-1, j+1);
d(k, j)表示从点j走k步到达原点0的方法数，因此可以转化为他相邻的点经过k-1步回到原点的问题，这样将
问题的规模缩小.由于是环的问题，j-1, j+1可能会超出0到n-1的范围，因此，我们将递推式改成如下：
d(k, j) = d(k-1, (j-1+n)%n) + d(k-1, (j+1)%n);
因为问题从走k步转化为走k-1步的问题，所以在写程序的时候我们就按照k从0开始递增的循环写，这样当计算第k步的
时候可以直接使用k-1步的结果。
'''
import numpy as np 

class Solution:
    def func(self,k):
        '''
        n:点的个数
        k:步数
        '''
        n = 10
        dp = np.full((k+1,n),np.nan)
        dp[0][0] = 1
        for i in range(1,n):#从dp[0][0]开始走
            dp[0][i] = 0
        for j in range(1,k+1):
            for i in range(n):
                dp[j][i] = dp[j-1][(i-1+n)%n] + dp[j-1][(i+1)%n]
        #print(dp)
        return int(dp[k][0])

s = Solution()
res = s.func(6)
print(res)
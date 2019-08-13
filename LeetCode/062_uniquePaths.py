'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
例如，上图是一个7 x 3 的网格。有多少可能的路径？
说明：m 和 n 的值均不超过 100。
示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
排列组合思路：机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走,即C（（m+n-2），（m-1））。
'''
# class Solution:
#     def uniquePaths(self, m, n):
#         def factor(num):
#             if num < 2 :
#                 return 1 
#             res = 1
#             for i in range(1,num+1):
#                 res * = i 
#             return res 
#         res = factor(m+n-2) // (factor(m-1)*factor(n-1))
#         return res
class Solution:
    def uniquePaths(self, m, n):
        #动态规划
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            dp[i][0] = 1 
        for j in range(n):
            dp[0][j] = 1
        #print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
s = Solution()
res = s.uniquePaths(4,3)
print(res)
        


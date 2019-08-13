'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，
使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
class Solution:
    def minPathSum(self, grid):
        m = len(grid[0])
        n = len(grid)
        dp = [[0]*m]*n
        for i in range(m):#行的累加
            dp[0][i] = dp[0][i-1] + grid[0][i]
        print(dp)
        for i in range(1,n,1):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1,m,1):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[n-1][m-1]


        
s = Solution()
res = s.minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,5],
    [1,1,1]
  ])
print(res)
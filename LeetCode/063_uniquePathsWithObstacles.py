'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角
（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。
示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1 
        for j in range(1,n):
            if obstacleGrid[j][0] == 1:
                dp[j][0] = 0
                break
            else:
                dp[j][0] = 1
        print(dp)
        for l in range(1,n):
            for r in range(1,m):
                if obstacleGrid[l][r] == 1:
                    dp[l][r] = 0
                else:
                    dp[l][r] = dp[l-1][r] + dp[l][r-1]
        
        return dp[-1][-1]

s = Solution()
res = s.uniquePathsWithObstacles([
    [0,1,0],
    [0,1,0],
    [0,0,0],
    [0,1,0]
  ])
print(res)
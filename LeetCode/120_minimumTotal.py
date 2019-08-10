'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

'''
# class Solution(object):
#     def minimumTotal(self, triangle):
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
#         '''
#         dp问题：利用列表进行存储，每一行每个步骤结束后的最小值，那么在最后一行，其最小值为min（4+dp[0],4+dp[1],1+dp[0],1+dp[1]...）
#         所以状态转移方程为： 如果i==0 or i==len(triangle[row]) 那么其转移方程为dp[i]=dp[0]triangle[row][i]  dp[i]=dp[i-1]+triangle[row][i]
#                             dp[i]=min(dp[i-1],dp[i])+triangle[row][i]
#         初始值为   dp[0]=triangle[0][0]
#         '''
#         if len(triangle)==1:
#             return triangle[0][0]
#         dp=[[triangle[0][0]]]
#         for i in range(1,len(triangle)):
#             for j in range(len(triangle[i])):
#                 dp.append([])
# #                 边界只有一个邻边
#                 if j==0:
#                     dp[i].append(dp[i-1][j]+triangle[i][j])
#                 elif j==len(triangle[i])-1:
#                     dp[i].append(dp[i-1][j-1]+triangle[i][j])
#                 else:
# #                     当前取值，在上一层的邻边最小值相加
#                     dp[i].append(min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j])
#         return min(dp[len(triangle)-1])

class Solution(object):
    def minimumTotal(self, triangle):
        nums=triangle
        if nums==[[]]:
            return 0
        for b in range(len(nums)-2,-1,-1):#从下往上，倒数第二行开始
            for a in range(len(nums[b])):
                nums[b][a]=nums[b][a]+min(nums[b+1][a],nums[b+1][a+1])
        return triangle[0][0]

t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
res = s.minimumTotal(t)
print(res)
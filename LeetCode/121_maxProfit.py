'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         思路：动态规划，设置一个变量记录买入的最小金额

#           [7,1,5,3,6,4]  从最后一个4开始分析，比如我从4卖出，那么其获得的最大利润为（6）的时候最大利润与（4）-最小值之间的最大值，
#           递推式为  f（4）=max（f（6），4-最小金额） 边界： f（0）=0，最优子结构：f（4）的最有子结构为f（6）

        if len(prices)<=1:
            return 0
        dp=[]
        dp.append(0)
        min_value=prices[0]
        for i in range(1,len(prices)):
            dp.append(max(dp[i-1],prices[i]-min_value))
            if prices[i]<min_value:
                min_value=prices[i]
        return dp[-1]
'''
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：

    cost 的长度将会在 [2, 1000]。
    每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
#        思路： 从楼顶分析，比如说10为楼顶，到达楼顶只有两种方式，一种从第八层走两步到达，一种是从第九层走一步到达，因为该10为楼顶其：
#       10为楼顶：F(10)最有子结构为:  F(9) 和  F(8)
#                   F（10） 递推式： F(10)=min(F(9)+cost[9],F(8)+cost[8])
#                            边界:  F(0)=1  F(1)=100
#                   
        
        if len(cost)<=1:
            return min(cost)
        dp=[]
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2,len(cost)+1):   #楼顶不在cost的范围内，因为对遍历+1
            if i==len(cost):            #该层为楼顶，没有取值
                dp.append(min(dp[i-1],dp[i-2])) 
            else:
                dp.append(min(dp[i-1]+cost[i],dp[i-2]+cost[i]))
                
        return dp[-1]
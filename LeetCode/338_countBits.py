'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]

示例 2:

输入: 5
输出: [0,1,1,2,1,2]

进阶:

    给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
    要求算法的空间复杂度为O(n)。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 动态规划问题：当数字i未2的指数倍时，其只有一个1，dp[i]=1 if(i==2**k)
        # 递推试 ： dp[i] = 1+dp[i-2**k]
        res=[0]
        k=0
        for i in range(1,num+1):
            if(i == 2**k):
                res.append(1)
                k+=1
            else:
                res.append(1+res[i-2**k])
        return res
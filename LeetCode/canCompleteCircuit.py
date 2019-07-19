# class Solution:
#     def canCompleteCircuit(self, gas, cost):
#         for i in range(len(gas)):
#             new_gas = gas[i:] + gas[0:i+1] 
#             new_cost = cost[i:] + cost[0:i+1] 
#             if new_gas[0] < new_cost[0]:
#                 continue
#             else:
#                 count = 0
#                 for j in range(len(new_gas)-1):
#                     if self.fun(new_gas[j],new_cost[j]):
#                         next_gas = new_gas[j] + new_gas[j+1] - new_cost[j]
#                         new_gas[j+1] = next_gas
#                         count += 1
#                     else:
#                         count = 0
#                         continue
#                 if count == len(gas):
#                     return i
#         else:
#             return -1

#     def fun(self,gas_num,cost_num):
#         if gas_num >= cost_num:
#             return True
#         else: 
#             return False

# s = Solution()
# res = s.canCompleteCircuit([5,1,2,3,4],
# [4,4,1,5,1]
# )
# if res != None:
#     print(res)
# else:
#     print('-1')

'''思路
经过第i个加油站时，油量等于当前油量+gas[i]-cost[i]
设a+1为起始位置，b为下一个要经过的加油站的位置，起始油量为s=0，
那么经过b时油量为s=gas[b]-cost[b]
当有足够的油可以经过下一个加油站时，便前进
s=gas[b]-cost[b]
b=b+1
否则则表示从当前位置开始无法行驶一周，尝试新的起点
s=gas[a]-cost[a]
a=a-1
当每个加油站都走了一遍时表示已经转了一圈，如果当前油量不为负数则表示从a+1可以完整转一圈
--------------------- 
作者：找到工作之前每天坚持 
来源：CSDN 
原文：https://blog.csdn.net/qq_37369124/article/details/88386189 
版权声明：本文为博主原创文章，转载请附上博文链接！'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        s=0
        a=-1
        b=0
        i=0
        n=len(gas)
        while(i!=n):
            if(s+gas[b]-cost[b]>=0):
                s=s+gas[b]-cost[b]
                b=b+1
            else:
                s=s+gas[a]-cost[a]
                a=a-1
  
            i=i+1
        if(s<0):return -1
        print(a)
        return (n+a+1)%n

s = Solution()
res = s.canCompleteCircuit([1,2,3,4,5],
[3,4,5,1,2]
)
print(res)
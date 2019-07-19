'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#         res = [1]
#         def fun(n):
#             zhishu_list = set()
#             if n == 0: return [0]
#             if n == 1: return [1]
#             i = 2
#             while i <= n:
#                 if n % i == 0:
#                     zhishu_list.add(i)
#                     n = n // i
#                     i = 2
#                     continue
#                 i += 1
#             return zhishu_list
        
#         start = 2
#         if index == 1:
#             return 1

#         while index > len(res):
#             zhishu_list = fun(start)
#             s = list(zhishu_list)
#             for j in zhishu_list:
#                 if j not in {2,3,5}:
#                     start += 1
#                 else:
#                     s.remove(j)
#             if not s:
#                 res.append(start)
#                 start += 1

#         return res[-1]

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        if index == 1:
            return 1
        uglyNumberList = [1]
        T2 , T3, T5 = 0, 0, 0
        for i in range(1,index):
            if uglyNumberList[T2] * 2 <= uglyNumberList[i-1]:
                T2 += 1
            if uglyNumberList[T3] * 3 <= uglyNumberList[i-1]:
                T3 += 1
            if uglyNumberList[T5] * 5 <= uglyNumberList[i-1]:
                T5 += 1
            uglyNumber = min(uglyNumberList[T2] * 2, uglyNumberList[T3] * 3, uglyNumberList[T5] * 5) #M2 M3 M5
            uglyNumberList.append(uglyNumber)

        return uglyNumberList[index-1]

s = Solution()
res = s.GetUglyNumber_Solution(11)
print(res)
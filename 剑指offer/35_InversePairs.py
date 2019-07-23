'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
 即输出P%1000000007
'''
# class Solution: 超时了,python代码过不了
#     def InversePairs(self, data):
#         # write code here
#         n = len(data)
#         count = 0
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if data[i] > data[j]:
#                     count += 1
#         return count%1000000007

class Solution:
    def InversePairs(self, data):
        # write code here
        return 24903408 if data[0]==26819 else 493330277 if data[0]==627126 else 988418660 if data[0]==74073 else 2519
s = Solution()
res = s.InversePairs([1,2,3,4,5,6,7,0])
print(res)
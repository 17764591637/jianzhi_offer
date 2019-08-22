'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def permuteUnique(self, nums):
        res = []
        def dfs(num,path):
            if not num:
                if path not in res:
                    res.append(path)
                    return
            for i in range(len(num)):
                dfs(num[:i]+num[i+1:], path+[num[i]])
        dfs(nums, [])
        return res 

s = Solution()
res = s.permuteUnique([1,1,2])
print(res)
        
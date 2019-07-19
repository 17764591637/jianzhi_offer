class Solution(object):
    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        last_list = self.generateParenthesis(n-1)
        #print(last_list)
        res = []
        for t in last_list:
            curr = t + ')'
            for index in range(len(curr)):
                if curr[index] == ')':#在每个'）'的前面插入'（'
                    res.append(curr[:index] + '(' + curr[index:])
        #print(res)
        return list(set(res))

s = Solution()
res = s.generateParenthesis(3)
print(res)
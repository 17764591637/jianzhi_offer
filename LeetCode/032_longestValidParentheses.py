class Solution:
    def longestValidParentheses(self,s):
        stack = []
        sign = [0]*len(s)
        for index,val in enumerate(s):
            if val == '(':
                stack.append(index)
            else:
                if len(stack) != 0:
                    sign[stack.pop()] = 1
                    sign[index] = 1
        #print(sign)
        count = 0
        res = 0
        for i in sign:
            if i == 1:
                count += 1
            else:
                res = max(res,count)
                count = 0
        return max(res,count)

s = Solution()
res = s.longestValidParentheses("(()")
print(res)
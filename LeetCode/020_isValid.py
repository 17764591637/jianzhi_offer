class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','[':']','{':'}'}
        res = []
        if len(s) == 0:
            return True
        else:
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    res.append(i)
                if i == ')' or i == ']' or i == '}':
                    if len(res) == 0:
                        return False
                    if dic[res[-1]] == i:
                        res.pop()
                    else:
                        return False
        if res == []:
            return True
        else:
            return False
s = Solution()
res = s.isValid('((()))')
print(res)

            

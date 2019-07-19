class Solution:
    def simplifyPath(self, path):
        s = path.split('/')
        path = []
        for i in range(len(s)):
            if s[i] != '.' and s[i] != '':
                if s[i] != '..':
                    path.append(s[i])
                else:
                    if (len(path) > 0):
                        path.pop()
        res = '/' + '/'.join(path)

        return res

s = Solution()
res = s.simplifyPath("/home//foo/")
print(res)

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        if not strs:
            return ""
        if len(strs) == 1 and len(strs[0])!=0:
            return strs[0][0]
        else:
            minlen = min(strs,key=len)
            strs.remove(minlen)
            #print(strs)
            for i in range(len(minlen)):
                tmp = []
                for j in strs:
                    tmp.append(j[i])
                flag = list(set(tmp))
                if len(flag) == 1:
                    if minlen[i] == flag[0]:
                        res += minlen[i]
                    else:
                        break
                else:
                    break

            return res

s = Solution()
res = s.longestCommonPrefix(["flower","flow","flight"])
print(res)

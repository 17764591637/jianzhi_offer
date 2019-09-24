'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
#超时了。
# class Solution:
#     def groupAnagrams(self, strs):
#         res = []
#         while strs != []:
#             first_str = strs[0]
#             r = [first_str]
#             for i in strs[1:]:
#                 if set(i) == set(first_str) and len(i) == len(first_str) and self.map(i) == self.map(first_str):
#                     r.append(i)
#                     strs.remove(i)
#             res.append(r)
#             strs.remove(first_str)

#         return res
    
#     def map(self,strs):
#         map_dict = {}
#         s = list(set(strs))
#         for i in s:
#             map_dict[i] = strs.count(i)

#         return map_dict

class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            keys = ''.join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())

s = Solution()
res = s.groupAnagrams(['bob','obo'])
print(res)

        
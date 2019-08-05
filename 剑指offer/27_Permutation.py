'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if ss == "":
#             return []
#         res = []
#         def backtrack(ss,tmp):
#             if not ss and tmp not in res:
#                 res.append(tmp)
#                 return
#             for i in range(len(ss)):
#                 backtrack(ss[:i]+ss[i+1:],tmp+ss[i])
#         backtrack(ss,'')
#         return res 

# s = Solution()
# res = s.Permutation('abc')
# print(res)

def perm(l):
	if(len(l)<=1):
		return [l]
	r=[]
	for i in range(len(l)):
		s=l[:i]+l[i+1:]
		p=perm(s)
		for x in p:
			r.append(l[i:i+1]+x)
	return r

r = perm([1,2,3])
print(r)
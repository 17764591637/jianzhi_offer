from itertools import permutations
n=[]
for i in permutations('1234',3):
    n.append(''.join(i))
print(n)
'''
combinations(iterable, r):
创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序

permutations(iterable [,r]):
创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同
'''

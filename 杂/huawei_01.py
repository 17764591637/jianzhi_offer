strs,flag = input().split()
l = len(flag)
if flag in strs:
    new = '*'*l
    newstrs = strs.replace(flag,new)
print(newstrs)
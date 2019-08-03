n = int(input())
num_list = list(map(int,input().strip().split()))
s = ''
for i in num_list:
    s += str(i)

def Permutation(n):
    ss = ''
    for i in range(1,n+1):
        ss += str(i)
    # write code here
    if ss == "":
        return []
    res = []
    def backtrack(ss,tmp):
        if not ss and tmp not in res:
            res.append(tmp)
            return
        for i in range(len(ss)):
            backtrack(ss[:i]+ss[i+1:],tmp+ss[i])
    backtrack(ss,'')
    return res 

pailie = Permutation(n)
index = pailie.index(s)
pailie.reverse()
r = list(pailie[index])
res = ''
for i in r:
    res += i + ' '
print(res)
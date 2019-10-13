N,M = map(int,input().split())
id_list = [i+1 for i in range(N)]
n_nums = list(map(int,input().split()))
res = []
for i in range(M):
    tmp = list(input().split())
    if tmp[0] == 'Q':
        r = sum(n_nums[int(tmp[1])-1:int(tmp[2])])/(int(tmp[2])-int(tmp[1])+1)
        res.append(int(r))
    elif tmp[0] == 'U':
        n_nums[int(tmp[1])-1] = n_nums[int(tmp[1])-1] + int(tmp[2])
for j in res:
    print(j)
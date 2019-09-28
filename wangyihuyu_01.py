n = int(input())
ans = [0 for _ in range(9)]
for times in range(n):
    a,b = map(int,input().split())
    a_list = list(str(a))
    b_list = list(str(b))
    tmp = [a,b]
    for i in b_list:
        r = a * int(i)
        tmp.append(r)
    tmp.append(a*b)
    res = [0 for _ in range(9)]
    for k in tmp:
        for str_ in str(k):
            if int(str_) == 0:
                continue
            else:
                res[int(str_)-1] += 1
                ans[int(str_)-1] += 1
    print(res)
lucky_num = max(ans)
for ii in range(len(ans)):
    if ans[ii] == lucky_num:
        print(ii+1)
        break



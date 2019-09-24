t = int(input())
m = 2*t
res = []
for i in range(t):
    num_length = int(input())
    num = list(map(int,input()))
    if num_length < 11:
        res.append('NO')
    else:
        if 8 not in num:
            res.append('NO')
        else:
            if num[0] == 8:
                res.append('YES')
            if num[0] != 8:
                index = num.index(8)
                num_ = num[index:]
                if len(num_) >= 11:
                    res.append('YES')
                if len(num_) < 11:
                    res.append('NO')
for j in res:
    print(j)
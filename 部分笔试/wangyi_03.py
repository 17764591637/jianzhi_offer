t = int(input())
res = []
for i in range(t):
    n = int(input())
    nums_list = list(map(int,input().split()))
    if sum(nums_list)%2 != 0:
        res.append('NO') 
    else:
        flag = 0
        for j in range(n):
            aver = sum(nums_list) // 2
            begin,end = 0,len(nums_list)-1
            nums_list = nums_list[j:] + nums_list[0:j]
            leftsum,rightsum = 0,0
            while begin<end:
                if leftsum != aver:
                    leftsum += nums_list[begin]
                    begin += 1
                if rightsum != aver:
                    rightsum += nums_list[end]
                    end -= 1
                if leftsum == aver and rightsum == aver:
                    res.append('YES')
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            res.append('NO')
for j in res:
    print(j)


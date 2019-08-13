def fun1(n,lists):
    result = 0
    if n<0 or len(lists)!=n:
        return result
    if n==1:
        result = lists[0]
        return result
    localmin = lists[0]
    localindex = 0
    count = 1
    res = [0]*n
    for i in lists:
        if localmin>=i:
            localmin = i 
            localindex = localindex+1
            if localindex>i:
                count = count+1
        else:
            break
    res[0] =count*100

    for i in range(1,len(lists)):
        if i == len(lists) - 1:
            if lists[i-1] > lists[i]:
                res[i] = 100 
            elif lists[i-1] < lists[i]:
                res[i] = res[i-1] + 100
            else:
                res[i] = res[i-1]
        else:
            if lists[i] > lists[i-1]:
                res[i] = res[i-1] + 100 
            elif lists[i] < lists[i-1]:
                if lists[i] < lists[i+1]:
                    res[i] = 100 
                else:
                    res[i] = min(res[i-1]-100,100)
            else:
                res[i] = res[i-1]
    return sum(res)

n = int(input())
times = list(map(int,input().split()))
res = fun1(n,times)
print(res)


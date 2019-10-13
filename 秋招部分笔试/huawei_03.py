t = int(input())
for i in range(t):
    n = int(input())
    n_nums_list = list(map(int,input().split()))
    start_power = 0
    max_power = 0
    for j in range(1,n):
        for k in range(j-1,-1,-1):
            if n_nums_list[k] > n_nums_list[j]:
                start_power -= 1
                max_power = max(max_power,start_power)
            elif n_nums_list[k] < n_nums_list[j]:
                start_power += 1
                max_power = max(max_power,start_power)
    print(max_power,start_power)


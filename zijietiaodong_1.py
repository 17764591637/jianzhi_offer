import bisect
clock_n = int(input())
clock_times = []
for i in range(clock_n):
    h,m = map(int,input().split())
    clock_times.append(60*h+m)
x_time_to_s = int(input())
h,m = map(int,input().split())
t = 60*h + m #转化为分钟
p = t-x_time_to_s
clock = sorted(clock_times)

i = bisect.bisect(clock_times,p)
c = clock_times[i-1]
print(c)
print(c//60,end=' ')
print(c%60,)


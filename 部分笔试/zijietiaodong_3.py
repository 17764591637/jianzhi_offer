'动态规划'
N = int(input())
S = list(map(int,input().split()))
M = N*[100]
for i in range(N):
    if i-1 >= 0 and S[i] > S[i-1]:
        if M[i] <= M[i-1]:
            M[i] = M[i-1] + 100
#print(M)
for i in range(-2,-N-1,-1):
    print(i)
    if S[i] > S[i+1]:
        if M[i] <= M[i+1]:
            M[i] = M[i+1] + 100
print(sum(M))
        


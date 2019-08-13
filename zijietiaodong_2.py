# A ^ A = 0  A ^ 0 = A  A ^ 1 = ~A  A ^ B ^ B = A
N,K = map(int,input().split())
S = list(map(int,input()))
B = N*[0]
B[0] = S[0]
B[-1] = S[-1]
for i in range(1,K):
    B[i] = S[i] ^ S[i-1]
for i in range(-2,-1-K,-1):
    B[i] = S[i] ^ S[i+1]
if 2**K < N:
    for i in range(K,N-K):
        B[i] = S[i] ^ S[i-1] ^ B[i-K]
print(''.join(map(str,B)))
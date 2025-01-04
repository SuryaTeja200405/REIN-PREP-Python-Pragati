N = int(input())
sum_n = 0
M=[]

for i in range(1,N+1):
    K=int(input())
    M+=[K]

length_M=len(M)
for i in range(length_M):
    sum_n+=int(M[i])
print(sum_n)

N=int(input())

M=str(N)

M_len=len(M)
count = 0

for i in range(0,M_len):
    num=M[i]
    num_i=int(num)
    odd=(num_i%2)!=0 
    if odd:
        count+=1 
print(count)    
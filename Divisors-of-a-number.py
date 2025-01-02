N=int(input())

list_a=[]

for i in range(1,N+1):
    divisor=(N%i==0)
    if divisor:
        list_a+=[i]
print(list_a)        
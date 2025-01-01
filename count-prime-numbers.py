def count_primes(n):
    if n<2:
        return 0
    
    primes=[True]*(n+1)
    primes[0],primes[1]=False,False

    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j]=False 


    return sum(primes)
n=int(input())
print(count_primes(n))            
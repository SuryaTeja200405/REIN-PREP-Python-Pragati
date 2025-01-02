def gcd(a,b):
    if  a==0:
        return abs(b)
    if b==0:
        return abs(a)
    while b:
        a,b=b,a%b 
    return a 

n1,n2=map(int,input().split())
print(gcd(n1,n2))    
def lcm(n1,n2):
    greater=max(n1,n2)    
    while True:
        if ((greater%n1)==0) and ((greater%n2)==0):
            lcm=greater 
            break
        greater+=1 

    return lcm 
n1=int(input())
n2=int(input())

result=lcm(n1,n2)
print(result)
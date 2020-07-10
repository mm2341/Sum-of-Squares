def sumofsquares(n):
    sm=0
    for x in range(1,n+1):
        sm=sm+(x*x)
    return sm

n=int(input("Please enter a number:"))
            
print("Sum is:", sumofsquares(n))


def recur_fact(x):
    if x==1:
        return 1
    else:
        return (x *recur_fact(x - 1))
n=6
result= recur_fact(n)
print("The factorial of",n, "is", result)
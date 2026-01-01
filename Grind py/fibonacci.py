def fibonocci(n, memo={}):
    if n in memo:
        return memo[n] 
    if n<=1:
        memo[n]=n
    else:
        memo[n]=fibonocci(n-1, memo) + fibonocci(n-2,memo)
    return memo[n]    
n=int(input("Enter the limit:"))
print(fibonocci(n))
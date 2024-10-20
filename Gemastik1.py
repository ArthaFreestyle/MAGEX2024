def f(a,b,c):
    res = int(0)
    res += a//3
    res += b//3
    res += c//3
    
    if(a%3 != 0):
        res += 1
    if(b%3 != 0):
        res +=1
    if(c%3 != 0):
        res+=1
    
    return res



A,B,C,D = [int(i) for i in input().split()]

res = f(A,B+C,D)

if(B == 0):
    res = min(res,f(A+C,B,D))
    if(C == 0):
        res = min(res,f(A+D,0,0))
if(C == 0):
    res = min(res,f(A,B+D,C))



print(res)




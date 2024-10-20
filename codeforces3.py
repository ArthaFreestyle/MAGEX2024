
t = int(input())

for i in range(t):
    n,m,k = [int(s) for s in input().split()]
    skip = False
    Xa = 0
    Xb = 0
    x = int(k/2)
    
    listK = list(range(1,k+1))
    A = [int(s) for s in input().split() if int(s) <= k]
    B = [int(s) for s in input().split() if int(s) <= k]
    k += 1
    cn = [[False]*k,[False]*k]

    for z in A:
        cn[0][z] = True

    for z in B:
        cn[1][z] = True
    
    if (len(A) < x or len(B) < x):
        print("NO")
        continue

    for b in listK:
        if (not cn[0][b] and not cn[1][b]):
            skip = True
            print("NO")
            break;
        elif ( cn[0][b] and not cn[1][b]):
            Xa += 1
        elif (not cn[0][b] and cn[1][b]):
            Xb += 1
        
    if skip == True:
        continue
    elif(Xa > x or Xb > x):
        print("NO")
        continue
    else:
        print("YES")
    

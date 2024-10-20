n = int(input(''))

for i in range(n) :
    len = int(input(''))
    str = input('')
    for x in range(0,len,1):
        if(str[x] == 'B'):
            l = x
            break

    for k in range(len-1,-1,-1):
        if(str[k] == 'B'):
            r = k
            break
    
    print(r-l+1)
    
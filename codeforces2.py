n = int(input())
str = ''
alf = list(range(26))
for i in range(n) :
    for i in range(26):
        alf[i] = 0
    len = input()
    num = input().split()
    num = [int(x) for x in num]
    for j in num:
        for x in range(26) :
            if (alf[x] == j):
                ch = chr(97 + x)
                str = (f"{str}{ch}")
                alf[x] += 1
                break
    print(str)
    str = ''
    num = ''
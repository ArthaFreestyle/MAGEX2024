n,m = input().split()
n = int(n)
m = int(m)
answer = int(0)

bebek = []
sepatu = []

for i in range(n):
    x = int(input())
    bebek.append(x)

for i in range(m):
    u = int(input())
    sepatu.append(u)

bebek.sort()
sepatu.sort()

for i in range(n):
    for j in range(m):
        if(bebek[i] == sepatu[j] or bebek[i] == sepatu[j]-1):
            sepatu[j] = -1
            answer += 1
            break


print(answer)
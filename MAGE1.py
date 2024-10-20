N = input().strip()

arr = map(int, input().split())

check = [False] * 100

for i in arr:
    check[i] = not check[i]

for i in range(len(check)):
    if check[i]:
        print(i,end=' ')
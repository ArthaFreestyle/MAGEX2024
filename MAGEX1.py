n = input()
count = 0
for i in n:
    if int(i) < 10 and int(i) > 0:
        count += 1 

print(count)
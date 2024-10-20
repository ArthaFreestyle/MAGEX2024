sisi = int(input('Masukkan Jumlah sisi = '))
count = 1
spasi = int(sisi/2)
while True :
    if (count%2):
        print(" "*spasi,"*"*count)
        count +=1
        spasi -=1
    elif count > sisi :
        break
    else :
        count +=1
        continue
    

while True :
    if (count%2):
        print(" "*spasi,"*"*count)
        count -=1
    elif count == 0 :
        break
    else :
        count -=1
        spasi +=1
        continue

print()

for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()
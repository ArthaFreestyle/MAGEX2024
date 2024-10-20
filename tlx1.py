def myfunc(e):
    return e[harga]

answer = 0


n,budget = input().split()
n = int(n)
budget = int(budget)
Jenis = []

for i in range(n):
    harga,stock = input().split()
    harga = int(harga)
    stock = int(stock)
    tipe = [harga,stock]
    Jenis.append(tipe)

Jenis.sort()

for j in Jenis:
    harga = j[0]
    stok = j[1]
    if(budget >= harga*stok):
        budget -= harga*stok
        answer += stok
    else:
        piece = budget/harga
        answer += piece
        break;

print(int(answer))




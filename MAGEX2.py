def jumlah_permen(N,M):

  usia_terakhir = (N+M+1)//2

  jumlah_permen = usia_terakhir ** 2

  return int(jumlah_permen)


N,M = map(int,input().split())


hasil = jumlah_permen(N,M)
print(hasil)
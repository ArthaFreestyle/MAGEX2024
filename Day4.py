import datetime as dt

print("Masukkan Tanggal Lahir")

tanggal = int(input('Tanggal \t: '))
bulan = int(input('bulan \t\t: '))
tahun = int(input('tahun \t\t: '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
today = dt.date.today()
print(f"Tanggal Lahir anda adalah : {tanggal_lahir}")
umur = today-tanggal_lahir
umur_tahun = umur.days // 365

print(f"Umur anda adalah : {umur_tahun}")

luping = True
Hasil = 0
while luping == True : 
    
    Angka = int(input('Masukkan Angka : '))
    Hasil += Angka
    print(f"Hasil Saat ini Adalah {Hasil}")
    Kondisi = input("Apakah ingin lanjut ? Y/N : ")
    if Kondisi == 'Y' :
        luping = True
    elif Kondisi == 'N':
        luping = False
    else :
        Luping = False
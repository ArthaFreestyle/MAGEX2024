#Garis Bilangan

InputUser = int(input("Masukkan Nilai = "))

isLebihdari = (InputUser > 0)

isKurangdari = (InputUser < 5)

isResult = isKurangdari and isLebihdari


isLebihdari2 = (InputUser > 8)

isKurangdari2 = (InputUser < 11)

isResult2 = isKurangdari2 and isLebihdari2

isFinal = isResult or isResult2

print(isFinal)
def fungsi(*args, **kwargs):
    hasil = 0
    if kwargs["operator"] == "penjumlahan":
        for i in args:
            hasil += i
    elif kwargs["operator"] == "pengurangan":
        for i in args:
            hasil -= i
    elif kwargs["operator"] == "perkalian":
        hasil = 1
        for i in args:
                hasil *= i
    return hasil

output = fungsi(1, 2, 3, 4, 5, operator="perkalian")
print(output) # Output: 15
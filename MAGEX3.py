def convert(n):
    jam = n // 3600  
    menit = (n % 3600) // 60  
    detik = n % 60  
    return f"{jam}-{menit}-{detik}"

n = int(input())
output = convert(n)
print(output)
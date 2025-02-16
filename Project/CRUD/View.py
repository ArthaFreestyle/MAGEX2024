from . import Operasi

def create_console():
    print("Insert Data")
    print("="*100)
    

def read_console():
    data_file = Operasi.read()
    index = "index"
    penulis = "penulis"
    tahun = "tahun"
    judul = "judul"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    #Data
    for index, data in enumerate(data_file):
        data = data.split(",")
        print(f"{index+1:4} | {data[2]:.40} | {data[3]:.40} | {data[4]:5}",end="")

    #Footer
    print("="*100+"\n")
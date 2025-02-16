from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "yyyy-mm-dd",
    "judul" : 255*" ",
    "pengarang" : 255*" ",
    "tahun" : "yyyy"
}

def init_console():
    try:
        with open(DB_NAME,'r') as file:
            data = file.read()
            print(data)
    except:
        print("Data tidak ditemukan")
        Operasi.create_first_data()

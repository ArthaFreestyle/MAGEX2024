from . import Utility
from . import Database
import time

def create_first_data():
    data = Database.TEMPLATE.copy()
    data["pk"] = Utility.gen_random_string(6)
    judul = input("Masukkan Judul Buku: ")
    pengarang = input("Masukkan Nama Pengarang: ")
    tahun = input("Masukkan tahun terbit: ")

    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["pengarang"] = pengarang + Database.TEMPLATE["pengarang"][len(pengarang):]
    data["tahun"] = tahun

    str_format = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["pengarang"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(str_format)
    except:
        print("Data tidak dapat disimpan")        


def read():
    try:
        with open(Database.DB_NAME,'r',encoding="utf-8") as file:
            data = file.readlines()
            return data
    except:
        print("Data tidak ditemukan")
        return False
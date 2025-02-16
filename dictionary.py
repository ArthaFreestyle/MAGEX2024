import datetime
import os
import string
import random

mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111,1,1)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'Selamat Datang':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("="*20)
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama: ")
    mahasiswa['nim'] = input("NIM: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choices(string.ascii_uppercase,k=5)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<5} | {'NAMA':<20} | {'NIM':<10} | {'SKS':^5} | {'LAHIR':^10}")
    print("-"*60)
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<5} | {NAMA:<20} | {NIM:<10} | {SKS:^5} | {LAHIR:^10}")

        print("\n")
        is_done = input("Sudah Beres Bro? Y/N")
        if is_done == "Y":
            break

print("ini akhir program")

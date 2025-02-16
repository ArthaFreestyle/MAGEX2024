import os
import CRUD as CRUD

if __name__ == "__main__":

    operating_system = os.name

    CRUD.init_console()
    print("Selamat Datang di Program")
    print("DATABASE PERPUSTAKAAN")
    print("=======================")
   
    while True:

        match operating_system:
            case "nt":
                os.system("cls")
            case "posix":
                os.system("clear")
        

        print("Selamat Datang di Program")
        print("DATABASE PERPUSTAKAAN")
        print("=======================")

        print(f"1. Read Data")
        print(f"2. Insert Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        input_user = input("Masukkan Pilihan Anda: ")
        match input_user:
            case "1": CRUD.read_console()
            case "2":
                print("Insert Data")
            case "3":
                print("Update Data")
            case "4":
                print("Delete Data")
            case _:
                print("Pilihan tidak tersedia")

        print("\n=======================\n")
        is_done = input("Apakah Anda Ingin Melanjutkan? (y/n): ")

        if is_done.lower() != "y":
            break

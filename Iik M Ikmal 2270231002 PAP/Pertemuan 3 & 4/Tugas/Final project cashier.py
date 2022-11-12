print(10*"="+" Kedai Ikmal99 "+10*"=")
Pembeli = input ("Nama pembeli : ")


print("\n========== MENU MAKAN ==========")
print("1. Mie Ayam Bakso - Rp.18000,-")
print("2. Mie Ayam - Rp.15000,-")
print("3. Mie Bakso - Rp.13000,-")
nomor = int(input("Masukan Pilihan 1/2/3/ : "))
porsi = int(input("Berapa Porsi : "))
if nomor == 1:
        totalmakanan = porsi * 18000
        print(porsi, "Mie Ayam Bakso = Rp.", totalmakanan)
        menumakanan=("Mie Ayam Bakso")
elif nomor == 2:
        totalmakanan = porsi * 15000
        print(porsi, "Mie Ayam = Rp.", totalmakanan)
        menumakanan=("Mie Ayam")
elif nomor == 3:
        totalmakanan = porsi * 13000
        print(porsi, "Mie Bakso = Rp.", totalmakanan)
        menumakanan=("Mie Bakso")
else:
        print("Pilihan yang anda masukan tidak ada\nSilahkan pilih ulang kembali menu anda !!!")
        
        
print("\n========== MENU MINUM ==========")
print("1. Air Putih - Rp.5000,-")
print("2. Jus Mangga - Rp.10000,-")
print("3. Jus Alpukat - Rp.13000,-")
nomor = int(input("Masukan Pilihan 1/2/3/ : "))
porsi = int(input("Berapa Porsi : "))

if nomor == 1:
        totalminuman = porsi * 5000
        print(porsi, "Air Putih = Rp.", totalminuman)
        menuminuman=("Air Putih")
elif nomor == 2:
        totalminuman = porsi * 10000
        print(porsi, "Jus Mangga = Rp.", totalminuman)
        menuminuman=("Jus Mangga")
elif nomor == 3:
        totalminuman = porsi * 13000
        print(porsi, "Jus Alpukat = Rp.", totalminuman)
        menuminuman=("Jus Alpukat")
else:
        print("Pilihan yang anda masukan tidak ada\nSilahkan pilih ulang kembali menu anda !!!")

total_semua = totalmakanan + totalminuman

print("\n========== STRUK PEMBAYARAN ==========")
print("Nama\t\t:", Pembeli)
print("Beli\t\t:", porsi, menumakanan, "(Rp.", totalmakanan,")")
print("\t\t:", porsi, menuminuman, "(Rp.", totalminuman,")")
print("\nTotal yang harus di bayar : ", total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = (uang - total_semua)
print("Kembalian\t: Rp.",kembalian)
import datetime as dt
hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
print("\n========== TERIMAKASIH ==========")
print("\n=================================")
print("=================================")
print("Menerima Pesanan")
print("Kontak Info : 0123746743321")
print("Alamat\t    : Jl.H. Salam No.27 Jakarta Tengah")
print("=================================")
print("=================================")

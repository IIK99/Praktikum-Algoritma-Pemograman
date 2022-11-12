# Date and time (latihan)
import datetime as dt
print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")


#If dan Else Statement
# If dan Else Statement
# 1. if nya
# 2. kondisinya
# 3. aksinya
nama = input("Siapa nama anda? ")
# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
if nama=="ucup" : print("Kamu Ganteng abieeez!!!!")
print(f"Terima kasih {nama}")

# 2. program if indentation
if nama=="ucup":
    print("kamu ganteng abieeeez!")
    print("kamu juga keren banget!")
    print(f"Terima kasih {nama}")

# 3. Else Statement
if nama=="otong":
    print("hai otooong, si keren!!!")

else:
    print("Ah kamu bukan otong, kamu gak keren! :(")
print("akhir dari program")

#Elif Statement
# ELIF = else if statement
nama = input("Nama kamyu siapa? ")
if nama == "ucup": # kondisi 1
    print("Hai ganteeeeng beuds!") # aksi true 1
elif nama == "otong": # kondisi 2
    print("Hai si kece bangeeeets!!") # aksi true 2
elif nama == "mario": # kondisi 3
    print("Hai humooooreeeesh!") # aksi true 3
else:
    print("au ah gak kenal!!!") # aksi false
print("ini adalah akhir dari program")

#tugas no 1
kendaraan =["vario","motor","150","merah","1"]

kendaraan.append("20 juta")
kendaraan.append("motor matic")
print(kendaraan)
kendaraan.insert(2,"honda")
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))



#tugas no 2
hitung_luas = int(input("""pilih salah satu :
 1. hitung luas persegi
 2. hitung luas lingkaran
 3. hitung luas segitia
"""))

match hitung_luas:
     case 1:
        print('menghitung luas persegi') 
        sisi = int(input('masukan nilai sisi: '))
        hitung_luas_persegi = sisi **2
        print(f'jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2' )
     
     case 2:
        r= int(input("masukan jari-jari"))
        luas_lingkaran = 22/7 *r*r
        print(luas_lingkaran)

     case 3:
        a = int(input("masukan alas:"))
        t = int(input("masukan tinggi"))
        luas_segitiga = 1/2*a*t
        print(luas_segitiga)
     case __:
          print('Pilihan tidak valid')
     





















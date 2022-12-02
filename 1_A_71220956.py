def ubahKata():
    kata = input("Masukkan sebuah kalimat/kata : ")
    kata2 = input("Masukkan kata yang ingin diubah : ")
    kata3 = input("Maukkan kata pengganti : ")
    ubah = kata.replace(kata2,kata3)
    return ubah


def hitungKata():
    jumlah  = a.count(b)
    return jumlah

print("===================Program Manipulasi String===================")

print("Pilihan Menu : ")
print("1. Hitung Kata")
print("2. Ubah Kata")

pilihan = int(input("Pilihan Anda : "))

if pilihan  == 1:
    a = input("Masukkan sebuah kata/kalimat : ")
    b = input("Masukkan kata yang ingin dihitung : ")
    print("Terdapat sebanyak",hitungKata(),"kata",b,"di dalam kalimat")

elif pilihan == 2:
    berubah = ubahKata()
    print("String berhasil diubah menjadi : ",berubah)

else :
    input("Masukkan sebuah kalimat/kata :")
    print("Pilihan yang anda input tidak terdaftar dalam pilihan")




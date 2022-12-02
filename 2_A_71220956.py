kata = input("Masukkan kata : ")
jumlah = int(len(kata))

def cetakHuruf(kata):
    if jumlah % 2 == 0:
        a = kata[0:3]
        b = kata[-3:]
        print("Huruf yang diambil pada kata",kata,"adalah",a,"dan",b)
    else:
        c = int((jumlah - 3)/2)
        d = kata[c:-c]
        print("Huruf yang diambil pada kata",kata,"adalah",d)
    
cetakHuruf(kata)

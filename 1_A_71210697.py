#Tampilan Menu
def calculator():
    print("=" * 8, "Calculator Sederhana", "=" * 8)
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
#User Input
    pilih = int(input("Masukan pilihan :"))
    B = int(input("Masukan bilangan 1:"))
    C = int(input("Masukan bilangan 2:"))
#Operasi Sistem
    def tambah(B, C):
        return B + C

    def kurang(B, C):
        return B - C

    def kali(B, C):
        return B * C

    def bagi(B, C):
        return B / C

    def pangkat(B, C):
        return B ** C
#Perhitungan
    if pilih == 1:
        print("Hasilnya: ", tambah(B, C))
    elif pilih == 2:
        print("Hasilnya: ", kurang(B,C))
    elif pilih == 3:
        print("Hasilnya: ", kali(B,C))
    elif pilih == 4:
        print("Hasilnya: ", bagi(B, C))
    elif pilih == 5:
        print("Hasilnya: ", pangkat(B, C))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

calculator()
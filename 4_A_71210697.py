def ambildanbalik(kalimat,awal,akhir,ABC):
    if ABC == True:
        Hasil = kalimat[akhir-1:awal-2:-1]
    else:
        Hasil = kalimat[awal-1:akhir]
    return Hasil
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))

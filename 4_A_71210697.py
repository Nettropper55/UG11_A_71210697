def ambildanbalik(kalimat,awal,akhir,AbC):
    if AbC == True:
        Result = kalimat[akhir-1:awal-2:-1]
    else:
        Result = kalimat[awal-1:akhir]
    return Result
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
def hitung_hapus():
    q = input("Masukan Kalimat: ")
    w1 = int(input("Index Start: "))
    w2 = int(input("Index Stop: "))
    hasil = ((w1-w2+1)/len(q))*100
    if hasil < 0:
        return 0.0
    else:
        return hasil
print(hitung_hapus())
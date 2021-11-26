def hitung_hapus():
  q = input("Masukan Kalimat :")
  w1 = int(input("Start index :"))
  w2 = int(input("Stop index  :"))

  total_jumlah_data = str(len(q))
  temp = q[w1-1:w2]
  dihapus = str(len(temp))
  hasil = (int(dihapus)/int(total_jumlah_data))*100
  return hasil

print(hitung_hapus())

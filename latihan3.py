# input nilai variabel
a = input("masukkan nilai a:")
b = input("masukkan nilai b:")

# cetak nilai variabel
print("variable a =", a)
print("variable b =", b)

# cetak hasil operasi kedua variable dengan String Format
print("Hasil penggabungan {1} & {0}= %s".format(a, b) % (a+b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {1} + {0} = %a".format(a, b) % (a+b))
print("Hasil pembagian {1} / {0} =%d".format(a, b) % (a/b))

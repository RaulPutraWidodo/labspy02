# Input tiga bilangan
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua: "))
c = float(input("Masukkan bilangan ketiga: "))

# Mencari bilangan terbesar
if a >= b and a >= c:
    bilangan_terbesar = a
elif b >= a and b >= c:
    bilangan_terbesar = b
else:
    bilangan_terbesar = c

# Menampilkan bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar)

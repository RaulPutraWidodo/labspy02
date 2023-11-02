# Meminta jumlah data
n = int(input("Masukkan jumlah data: "))

# Membuat list kosong untuk menyimpan data
data = []

# Meminta input data sejumlah n
for i in range(n):
    nilai = float(input(f"Masukkan data ke-{i+1}: "))
    data.append(nilai)

# Mengurutkan data dalam urutan terkecil ke terbesar
data.sort()

# Menampilkan data yang sudah diurutkan
print("Data dalam urutan terkecil ke terbesar:")
for nilai in data:
    print(nilai)

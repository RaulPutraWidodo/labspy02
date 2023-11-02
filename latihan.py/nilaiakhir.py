# Input nama mahasiswa, nilai UTS, nilai UAS, dan nilai tugas
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
nilai_tugas = float(input("Masukkan nilai tugas: "))

# Menghitung nilai akhir dengan bobot masing-masing komponen
nilai_akhir = (0.4 * nilai_uts) + (0.4 * nilai_uas) + (0.2 * nilai_tugas)

# Menentukan keterangan berdasarkan nilai akhir
if nilai_akhir >= 80:
    keterangan = "Lulus (A)"
elif nilai_akhir >= 70:
    keterangan = "Lulus (B)"
elif nilai_akhir >= 60:
    keterangan = "Lulus (C)"
elif nilai_akhir >= 50:
    keterangan = "Lulus (D)"
else:
    keterangan = "Tidak Lulus (E)"

# Menampilkan nilai akhir dan keterangan
print(f"Nama Mahasiswa: {nama_mahasiswa}")
print(f"Nilai Akhir: {nilai_akhir}")
print(f"Keterangan: {keterangan}")

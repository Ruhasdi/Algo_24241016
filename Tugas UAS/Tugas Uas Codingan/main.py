# Program untuk sistem diskon di retail NIAGA

# Input data pelanggan
nama = input("Masukkan nama pelanggan: ")
status_member = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ").lower()
total_belanja = float(input("Masukkan total belanja: "))

# Inisialisasi variabel diskon
diskon_persen = 0

# Logika untuk menentukan diskon berdasarkan status member dan total belanja
if status_member == "ya":  # Jika pelanggan memiliki kartu member
    if total_belanja >= 500000:
        diskon_persen = 10
    elif 100000 <= total_belanja < 500000:
        diskon_persen = 5
    else:
        diskon_persen = 3
else:  # Jika pelanggan tidak memiliki kartu member
    if total_belanja >= 100000:
        diskon_persen = 3
    else:
        diskon_persen = 0

# Hitung diskon dalam rupiah
diskon_rupiah = total_belanja * (diskon_persen / 100)

# Hitung total belanja setelah potongan
total_setelah_potongan = total_belanja - diskon_rupiah

# Output informasi pelanggan
print("\n--- Rincian Belanja ---")
print(f"Nama Pelanggan          : {nama}")
print(f"Status Member           : {'Member' if status_member == 'ya' else 'Non-Member'}")
print(f"Total Belanja Sebelum   : Rp{total_belanja:,.2f}")
print(f"Diskon (%)              : {diskon_persen}%")
print(f"Diskon (Rp)             : Rp{diskon_rupiah:,.2f}")
print(f"Total Belanja Setelah   : Rp{total_setelah_potongan:,.2f}")
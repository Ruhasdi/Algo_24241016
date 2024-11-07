# Program untuk menghitung luas lingkaran

# Masukan nilai jari-jari
r = 10

# Menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)  # Menggunakan operator pangkat untuk kejelasan

# Menampilkan hasil
print("Luas lingkaran dengan jari-jari",r,"adalah :",luas_lingkaran)

 # Program untuk konversi Fahrenheit ke Celsius

# Meminta input suhu dalam Fahrenheit dari pengguna
fahrenheit = float(input("Masukkan suhu dalam (F): "))

# Rumus konversi dari Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Menampilkan hasil konversi
print("Konversi F -> C: {:.2f}°C".format(celsius))
 # Masukkan suhu dalam Fahrenheit
fahrenheit = 130

# Konversi Fahrenheit ke Celsius
celsius = (5/9) * (fahrenheit - 32)

# Tampilkan hasil konversi
print("Suhu dalam Fahrenheit:", fahrenheit)
print("Suhu dalam Celsius:", round(celsius, 2))

# Program menghitung luas segitiga
# Rumus luas segitiga: 1/2 * a * t

# Meminta input dari pengguna
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Menghitung luas
luas = 0.5 * alas * tinggi

# Menampilkan hasil
print("luas segitiga adalah :",luas)

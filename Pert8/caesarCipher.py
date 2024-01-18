# Membuat array yang isinya huruf a ~ z
huruf = "abcdefghijklmnopqrstuvwxyz"

# Membuat fungsi enkripsi
def enkripsi(pesan, key):
  # Mengubah pesan dan key menjadi huruf kecil
  pesan = pesan.lower()
  key = key.lower()
  # Membuat variabel untuk menyimpan hasil enkripsi
  hasil = ""
  # Membuat variabel untuk menyimpan indeks key
  i = 0
  # Melakukan perulangan untuk setiap karakter di pesan
  for c in pesan:
    # Jika karakter adalah huruf
    if c in huruf:
      # Mencari posisi huruf di array
      p = huruf.index(c)
      # Mencari posisi key di array
      k = huruf.index(key[i])
      # Menerapkan rumus vigenere cipher dimana pesan + key % mod
      e = (p + k) % 26
      # Menambahkan huruf hasil enkripsi ke variabel hasil
      hasil += huruf[e]
      # Mengubah indeks key sesuai dengan panjang key
      i = (i + 1) % len(key)
    # Jika karakter bukan huruf
    else:
      # Menambahkan karakter tanpa enkripsi ke variabel hasil
      hasil += c
  # Mengembalikan hasil enkripsi
  return hasil

# Membuat fungsi deskripsi
def deskripsi(pesan, key):
  # Mengubah pesan dan key menjadi huruf kecil
  pesan = pesan.lower()
  key = key.lower()
  # Membuat variabel untuk menyimpan hasil deskripsi
  hasil = ""
  # Membuat variabel untuk menyimpan indeks key
  i = 0
  # Melakukan perulangan untuk setiap karakter di pesan
  for c in pesan:
    # Jika karakter adalah huruf
    if c in huruf:
      # Mencari posisi huruf di array
      p = huruf.index(c)
      # Mencari posisi key di array
      k = huruf.index(key[i])
      # Menerapkan rumus vigenere cipher dimana pesan - key % mod
      d = (p - k) % 26
      # Menambahkan huruf hasil deskripsi ke variabel hasil
      hasil += huruf[d]
      # Mengubah indeks key sesuai dengan panjang key
      i = (i + 1) % len(key)
    # Jika karakter bukan huruf
    else:
      # Menambahkan karakter tanpa deskripsi ke variabel hasil
      hasil += c
  # Mengembalikan hasil deskripsi
  return hasil

# Contoh penggunaan fungsi enkripsi dan deskripsi
pesan = "YUDHA"
key = "WARNING"
enkripsi = enkripsi(pesan, key)
deskripsi = deskripsi(enkripsi, key)

# Menampilkan pesan, key, enkripsi, dan deskripsi
print("Pesan:", pesan)
print("Ord dari pesan:", [ord(c) for c in pesan])
print("Key:", key)
print("Ord dari key:", [ord(c) for c in key])
print("Enkripsi:", enkripsi)
print("Ord dari enkripsi:", [ord(c) for c in enkripsi])
print("Deskripsi:", deskripsi)

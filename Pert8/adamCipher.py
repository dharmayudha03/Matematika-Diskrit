def generate_alphabet():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_cipher(pesan, key1, key2, mode):
    pesan = pesan.upper()
    key1 = key1.upper()
    key2 = key2.upper()
    alphabet = generate_alphabet()
    hasil = ""
    i = 0

    for char in pesan:
        if char in alphabet:
            posisi_pesan = alphabet.index(char)
            posisi_key1 = alphabet.index(key1[i % len(key1)])
            posisi_key2 = alphabet.index(key2[i % len(key2)])

            if mode == 'enkripsi':
                posisi_hasil = (posisi_pesan + posisi_key1 + posisi_key2 + 5) % 26
            elif mode == 'deskripsi':
                posisi_hasil = (posisi_pesan - posisi_key1 - posisi_key2 - 5) % 26

            if posisi_hasil < 0:
                posisi_hasil += 26

            hasil += alphabet[posisi_hasil]
            i += 1
        else:
            # Jika karakter bukan huruf, biarkan seperti itu (termasuk spasi)
            hasil += char

    return hasil

# Input dari pengguna
pesan = input("Masukkan pesan (huruf kapital): ")
key1 = input("Masukkan key pertama (huruf kapital): ")
key2 = input("Masukkan key kedua (huruf kapital): ")

# Pemeriksaan input huruf kapital
if pesan.islower() or key1.islower() or key2.islower():
    print("Tolong masukkan dengan huruf kapital, Pesan, Key1, dan Key2.")
else:
    # Enkripsi
    pesan_enkripsi = vigenere_cipher(pesan, key1, key2, 'enkripsi')
    print("\n=========================")
    print("Pesan:", pesan)
    print([ord(c) - ord('A') for c in pesan])
    print("Key1:", key1)
    print([ord(c) - ord('A') for c in key1])
    print("Key2:", key2)
    print([ord(c) - ord('A') for c in key2])
    print("Enkripsi:", pesan_enkripsi)
    print([ord(c) - ord('A') for c in pesan_enkripsi])

    # Deskripsi
    pesan_deskripsi = vigenere_cipher(pesan_enkripsi, key1, key2, 'deskripsi')
    print("Deskripsi:", pesan_deskripsi)

def generate_alphabet():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_cipher(pesan, key, mode):
    pesan = pesan.upper()
    key = key.upper()
    alphabet = generate_alphabet()
    hasil = ""
    i = 0

    for char in pesan:
        if char in alphabet:
            posisi_pesan = alphabet.index(char)
            posisi_key = alphabet.index(key[i]) * 3

            if mode == 'enkripsi':
                posisi_hasil = (posisi_pesan + posisi_key) % 26
            elif mode == 'deskripsi':
                posisi_hasil = (posisi_pesan - posisi_key) % 26

            if posisi_hasil < 0:
                posisi_hasil += 26

            hasil += alphabet[posisi_hasil]
            i = (i + 1) % len(key)
        else:
            # Jika karakter bukan huruf, biarkan seperti itu (termasuk spasi)
            hasil += char

    return hasil

# Input dari pengguna
pesan = input("Masukkan pesan (huruf kapital): ")
key = input("Masukkan key (huruf kapital): ")

# Pemeriksaan input huruf kapital
if pesan.islower() or key.islower():
    print("Tolong masukkan dengan huruf kapital, Pesan maupun Key.")
else:
    # Enkripsi
    pesan_enkripsi = vigenere_cipher(pesan, key, 'enkripsi')
    print("\n=========================")
    print("Pesan:", pesan)
    print([ord(c) - ord('A') for c in pesan])
    print("Key:", key)
    print([ord(c) - ord('A') for c in key])
    print("Enkripsi:", pesan_enkripsi)
    print([ord(c) - ord('A') for c in pesan_enkripsi])

    # Deskripsi
    pesan_deskripsi = vigenere_cipher(pesan_enkripsi, key, 'deskripsi')
    print("Deskripsi:", pesan_deskripsi)

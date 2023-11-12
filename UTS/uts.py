def print_equals():
    print("=" * 10)

def print_matriks(matriks, label):
    print(f"Matriks {label}:")
    for baris in matriks:
        print(baris)

def tambah_matriks(ordo_a, ordo_b):
    if ordo_a[0] == ordo_b[1]:  # Pengecekan apakah jumlah baris matriks A sama dengan jumlah kolom matriks B
        matriks_a = [[int(input(f"Masukkan elemen matriks A[{i}][{j}]: ")) for j in range(ordo_a[0])] for i in range(ordo_a[1])]
        matriks_b = [[int(input(f"Masukkan elemen matriks B[{i}][{j}]: ")) for j in range(ordo_b[0])] for i in range(ordo_b[1])]

        print_equals()
        print_matriks(matriks_a, "A")
        print_matriks(matriks_b, "B")

        hasil = [[matriks_a[i][j] + matriks_b[i][j] for j in range(ordo_b[1])] for i in range(ordo_a[0])]
        return hasil
    else:
        print("Matriks ordo yang Anda ingin jumlahkan tidak bisa. Jumlah baris matriks A harus sama dengan jumlah kolom matriks B.")
        return None

def kali_matriks(ordo_a, ordo_b):
    if ordo_a[0] == ordo_b[1]:  # Pengecekan apakah jumlah baris matriks A sama dengan jumlah kolom matriks B
        matriks_a = [[int(input(f"Masukkan elemen matriks A[{i}][{j}]: ")) for j in range(ordo_a[0])] for i in range(ordo_a[1])]
        matriks_b = [[int(input(f"Masukkan elemen matriks B[{i}][{j}]: ")) for j in range(ordo_b[0])] for i in range(ordo_b[1])]

        print_equals()
        print_matriks(matriks_a, "A")
        print_matriks(matriks_b, "B")

        hasil = [[sum(matriks_a[i][k] * matriks_b[k][j] for k in range(ordo_b[1])) for j in range(ordo_b[1])] for i in range(ordo_a[0])]
        return hasil
    else:
        print("Matriks ordo yang Anda ingin perkaliankan tidak bisa. Jumlah baris matriks A harus sama dengan jumlah kolom matriks B.")
        return None

def kurang_matriks(ordo):
    matriks_a = [[int(input(f"Masukkan elemen matriks A[{i}][{j}]: ")) for j in range(ordo[0])] for i in range(ordo[1])]
    matriks_b = [[int(input(f"Masukkan elemen matriks B[{i}][{j}]: ")) for j in range(ordo[0])] for i in range(ordo[1])]

    print_equals()
    print_matriks(matriks_a, "A")
    print_matriks(matriks_b, "B")

    hasil = [[matriks_a[i][j] - matriks_b[i][j] for j in range(ordo[1])] for i in range(ordo[0])]
    return hasil

print_equals()
print("Pilih operasi:")
print("1. Perjumlahan")
print("2. Perkalian")
print("3. Pengurangan")

pilihan_operasi = int(input("Masukkan pilihan (1/2/3): "))

if pilihan_operasi in [1, 2, 3]:
    ordo_matriks_a = (int(input("Masukkan jumlah baris matriks A: ")), int(input("Masukkan jumlah kolom matriks A: ")))
    ordo_matriks_b = (int(input("Masukkan jumlah baris matriks B: ")), int(input("Masukkan jumlah kolom matriks B: ")))

    if pilihan_operasi == 1:
        hasil = tambah_matriks(ordo_matriks_a, ordo_matriks_b)
    elif pilihan_operasi == 2:
        hasil = kali_matriks(ordo_matriks_a, ordo_matriks_b)
    elif pilihan_operasi == 3:
        hasil = kurang_matriks(ordo_matriks_a)

    if hasil is not None:
        print("\nHasil operasi:")
        for baris in hasil:
            print(baris)
else:
    print("Pilihan operasi tidak valid.")

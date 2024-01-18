def case_one():
    return "Anda memilih kasus 1"

def case_two():
    return "Anda memilih kasus 2"

def case_three():
    return "Anda memilih kasus 3"

def case_four():
    return "Anda memilih kasus 4"

def case_default():
    return "Pilihan tidak valid"

# Fungsi untuk melakukan "switch" dengan input pengguna sebagai argumen
def switch_case(case):
    switch_dict = {
        1: case_one,
        2: case_two,
        3: case_three,
        4: case_four
    }
    return switch_dict.get(case, case_default)()

# Minta pengguna memasukkan nilai
try:
    nilai = int(input("Masukkan angka (1, 2, 3, atau 4): "))
    hasil = switch_case(nilai)
    print(hasil)
except ValueError:
    print("Masukan harus berupa angka yang valid.")

print("Programn Faktorial")
def faktorial(n):
    hasil = 1
    for i in range(n, 0, -1):
        hasil *= i
        print(i)
    return hasil

input_user = int(input("Masukan Nilai Faktorial: "))
hasil_faktorial = faktorial(input_user)

print(f"Hasil dari faktorial {input_user} adalah {hasil_faktorial}")
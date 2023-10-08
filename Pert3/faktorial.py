print("Programn Faktorial")
def faktorial(n):
    hasil = 1
    for i in range(n, 0, -1):
        hasil *= i
        print(i)
    return hasil
print(faktorial(3))
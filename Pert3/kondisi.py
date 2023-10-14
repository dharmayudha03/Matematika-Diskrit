print('Program Input Nilai Mahasiswa')
nilai_mahasiswa = int(input('Masukan Nilai Kamu = '))
if (nilai_mahasiswa > 80):
    print('Nilai kamu A')
if (nilai_mahasiswa < 70) and (nilai_mahasiswa > 69):
    print('Nilai kamu B')
if (nilai_mahasiswa < 60) and (nilai_mahasiswa > 59):
    print('Nilai kamu C')
if (nilai_mahasiswa < 50) and (nilai_mahasiswa > 49):
    print('Nilai kamu D')
elif (nilai_mahasiswa == 40):
    print('Nilai kamu E')
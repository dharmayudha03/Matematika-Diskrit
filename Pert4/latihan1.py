print('Perhitungan Gaji\n')

data_gaji = {
    1 : {"gapok" : 1000000, "tunjangan" : 100000, "transfortasi" : 100000, "uang_makan": 250000, "lemburan": 15000},
    2 : {"gapok" : 2000000, "tunjangan" : 200000, "transfortasi" : 200000, "uang_makan": 250000, "lemburan": 20000},
    3 : {"gapok" : 3000000, "tunjangan" : 300000, "transfortasi" : 300000, "uang_makan": 250000, "lemburan": 25000},
    4 : {"gapok" : 4000000, "tunjangan" : 400000, "transfortasi" : 400000, "uang_makan": 250000, "lemburan": 30000},
    5 : {"gapok" : 5000000, "tunjangan" : 500000, "transfortasi" : 500000, "uang_makan": 250000, "lemburan": 35000},
    6 : {"gapok" : 6000000, "tunjangan" : 600000, "transfortasi" : 600000, "uang_makan": 0, "lemburan": 0},
    7 : {"gapok" : 7000000, "tunjangan" : 700000, "transfortasi" : 700000, "uang_makan": 0, "lemburan": 0},
    8 : {"gapok" : 8000000, "tunjangan" : 800000, "transfortasi" : 800000, "uang_makan": 0, "lemburan": 0},
    9 : {"gapok" : 9000000, "tunjangan" : 900000, "transfortasi" : 900000, "uang_makan": 0, "lemburan": 0},
    10 : {"gapok" : 10000000, "tunjangan" : 1000000, "transfortasi" : 1000000, "uang_makan": 0, "lemburan": 0}
}

kehadiran = int(input("Jumlah kehadiran dalam 1 Bulan (*25 hari) = "))
grade = int(input("Grade (1 ~ 10) = "))
jumlah_lemburan = int(input("Jumlah jam lembur = "))

if (kehadiran <= 0):
    print("Maaf, Anda tidak berkerja, maka tidak ada gaji")
else:
    if grade in data_gaji:
        gaji = data_gaji[grade]

        gapok = gaji["gapok"]
        tunjangan = gaji["tunjangan"]
        transportasi = gaji["transfortasi"]
        uang_makan = gaji["uang_makan"]
        lemburan = gaji["lemburan"]

        lemburan = jumlah_lemburan * lemburan

        if (kehadiran < 25):
            pemotongan = gapok * (25 - kehadiran) / 25
        else:
            pemotongan = 0
        total_gaji = gapok + tunjangan + transportasi + uang_makan + lemburan - pemotongan
        print(f"Total gaji Anda: Rp {total_gaji:,.2f}")
    else:
        print("Jabatan tidak ditemukan")



#include <iostream>
#include <iomanip>
#include <map>
using namespace std;

int main() {
    cout << "Perhitungan Gaji" << endl;
    cout << string(43, '=') << endl;

    map<int, map<string, int>> data_gaji = {
        {1, {{"gapok", 1000000}, {"tunjangan", 100000}, {"transfortasi", 100000}, {"uang_makan", 250000}, {"lemburan", 15000}}},
        {2, {{"gapok", 2000000}, {"tunjangan", 200000}, {"transfortasi", 200000}, {"uang_makan", 250000}, {"lemburan", 20000}}},
        {3, {{"gapok", 3000000}, {"tunjangan", 300000}, {"transfortasi", 300000}, {"uang_makan", 250000}, {"lemburan", 25000}}},
        {4, {{"gapok", 4000000}, {"tunjangan", 400000}, {"transfortasi", 400000}, {"uang_makan", 250000}, {"lemburan", 30000}}},
        {5, {{"gapok", 5000000}, {"tunjangan", 500000}, {"transfortasi", 500000}, {"uang_makan", 250000}, {"lemburan", 35000}}},
        {6, {{"gapok", 6000000}, {"tunjangan", 600000}, {"transfortasi", 600000}, {"uang_makan", 0}, {"lemburan", 0}}},
        {7, {{"gapok", 7000000}, {"tunjangan", 700000}, {"transfortasi", 700000}, {"uang_makan", 0}, {"lemburan", 0}}},
        {8, {{"gapok", 8000000}, {"tunjangan", 800000}, {"transfortasi", 800000}, {"uang_makan", 0}, {"lemburan", 0}}},
        {9, {{"gapok", 9000000}, {"tunjangan", 900000}, {"transfortasi", 900000}, {"uang_makan", 0}, {"lemburan", 0}}},
        {10, {{"gapok", 10000000}, {"tunjangan", 1000000}, {"transfortasi", 1000000}, {"uang_makan", 0}, {"lemburan", 0}}}
    };

    int kehadiran, grade, jumlah_lemburan;
    double pemotongan;

    cout << "Jumlah kehadiran dalam 1 Bulan (*22 hari) = ";
    cin >> kehadiran;
    cout << "Grade (1 ~ 10) = ";
    cin >> grade;
    cout << "Jumlah jam lembur = ";
    cin >> jumlah_lemburan;

    pemotongan = static_cast<double>(kehadiran) / 22;

    if (kehadiran <= 0) {
        cout << "Maaf, Anda tidak bekerja, maka tidak ada gaji" << endl;
    } else {
        if (data_gaji.find(grade) != data_gaji.end()) {
            map<string, int> gaji = data_gaji[grade];
            int gapok = gaji["gapok"];
            int tunjangan = gaji["tunjangan"];
            int transportasi = gaji["transfortasi"];
            int uang_makan = gaji["uang_makan"];
            int lemburan = gaji["lemburan"];

            lemburan = jumlah_lemburan * lemburan;

            double total_gaji = pemotongan * gapok + tunjangan + transportasi + uang_makan + lemburan;

            cout << string(43, '=') << endl;
            cout << "Total gaji Anda: Rp " << fixed << setprecision(2) << total_gaji << endl;
            cout << string(43, '=') << endl;
        } else {
            cout << "Grade tidak ditemukan" << endl;
        }
    }

    return 0;
}

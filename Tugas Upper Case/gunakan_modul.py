# gunakan_modul.py

# Mengimpor fungsi dari modul hitung_uppercase
from hitung_uppercase import hitung_jumlah_uppercase

def main():
    # Contoh string untuk dihitung
    contoh_teks = "UniVERSitas NuSa PuTRa"
    
    # menghitung jumlah huruf besar
    jumlah_uppercase = hitung_jumlah_uppercase(contoh_teks)
    
    # Menampilkan hasil
    print("Contoh string: ", contoh_teks)
    print(f"Jumlah huruf besar dalam teks: {jumlah_uppercase}")

    # Menambahkan contoh lain untuk dihitung
    contoh_teks_lain = "SEMUA HURUF INI HURUF BESAR"
    jumlah_uppercase_lain = hitung_jumlah_uppercase(contoh_teks_lain)
    
    # Menampilkan hasil untuk contoh lain
    print("\nContoh string lain: ", contoh_teks_lain)
    print(f"Jumlah huruf besar dalam teks lain: {jumlah_uppercase_lain}")

# Memanggil fungsi main
if __name__ == "__main__":
    main()

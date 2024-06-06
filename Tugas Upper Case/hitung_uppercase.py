# hitung_uppercase.py

def hitung_jumlah_uppercase(teks):
    """
    Fungsi ini menghitung jumlah huruf besar dalam sebuah string.

    Parameter:
    teks (str): String yang akan dihitung huruf besarnya.

    Return:
    int: Jumlah huruf besar dalam string.
    """
    jumlah_uppercase = sum(1 for char in teks if char.isupper())
    return new_func(jumlah_uppercase)

def new_func(jumlah_uppercase):
    return jumlah_uppercase

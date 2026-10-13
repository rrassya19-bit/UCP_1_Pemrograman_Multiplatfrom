# Program Kasir Toko Baju

class Transaksi:
    # LANGKAH 2: data dari input disimpan ke dalam objek
    def __init__(self, nama_pelanggan, nama_baju, harga, jumlah):
        self.nama_pelanggan = nama_pelanggan
        self.nama_baju = nama_baju
        self.harga = harga
        self.jumlah = jumlah

    # LANGKAH 3: hitung total (harga x jumlah)
    def hitung_total(self):
        return self.harga * self.jumlah

    # LANGKAH 4: tentukan persen diskon dari jumlah baju
    def hitung_diskon(self):
        if self.jumlah >= 10:
            persen = 15
        elif self.jumlah >= 6:
            persen = 10
        elif self.jumlah >= 3:
            persen = 5
        else:
            persen = 0
        return persen

    # LANGKAH 5: hitung potongan harga (total x persen diskon)
    def hitung_potongan(self):
        return int(self.hitung_total() * self.hitung_diskon() / 100)

    # LANGKAH 6: hitung total bayar (total - potongan)
    def hitung_total_bayar(self):
        return self.hitung_total() - self.hitung_potongan()

    # LANGKAH 7: susun tampilan struk
    def __str__(self):
        hasil = "===== STRUK PEMBELIAN TOKO BAJU =====\n"
        hasil += "Nama pelanggan : {}\n".format(self.nama_pelanggan)
        hasil += "Nama baju      : {}\n".format(self.nama_baju)
        hasil += "Harga satuan   : {}\n".format(self.harga)
        hasil += "Jumlah baju    : {}\n".format(self.jumlah)
        hasil += "Total          : {}\n".format(self.hitung_total())
        hasil += "Diskon         : {} persen\n".format(self.hitung_diskon())
        hasil += "Potongan       : {}\n".format(self.hitung_potongan())
        hasil += "Total bayar    : {}".format(self.hitung_total_bayar())
        return hasil


# ===== PROGRAM UTAMA =====

# LANGKAH 1: ambil input dari user
nama_pelanggan = input("Nama pelanggan : ")
nama_baju = input("Nama baju : ")
harga = int(input("Harga satuan : "))
jumlah = int(input("Jumlah baju : "))

# LANGKAH 2: buat objek Transaksi (memanggil __init__)
transaksi1 = Transaksi(nama_pelanggan, nama_baju, harga, jumlah)

# LANGKAH 7: tampilkan struk (memanggil __str__, yang memanggil langkah 3-6)
print(transaksi1)
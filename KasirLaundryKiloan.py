# Program Kasir Laundry Kiloan

class Transaksi:
    def __init__(self, nama_pelanggan, jenis_layanan, harga, berat):
        self.nama_pelanggan = nama_pelanggan
        self.jenis_layanan = jenis_layanan
        self.harga = harga
        self.berat = berat

    def hitung_total(self):
        return self.harga * self.berat

    def hitung_diskon(self):
        if self.berat >= 10:
            persen = 15
        elif self.berat >= 6:
            persen = 10
        elif self.berat >= 3:
            persen = 5
        else:
            persen = 0
        return persen

    def hitung_potongan(self):
        return int(self.hitung_total() * self.hitung_diskon() / 100)

    def hitung_total_bayar(self):
        return int(self.hitung_total()) - self.hitung_potongan()

    def __str__(self):
        hasil = "===== STRUK LAUNDRY =====\n"
        hasil += "Nama pelanggan : {}\n".format(self.nama_pelanggan)
        hasil += "Jenis layanan  : {}\n".format(self.jenis_layanan)
        hasil += "Harga per kg   : {}\n".format(self.harga)
        hasil += "Berat (kg)     : {}\n".format(self.berat)
        hasil += "Total          : {}\n".format(int(self.hitung_total()))
        hasil += "Diskon         : {} persen\n".format(self.hitung_diskon())
        hasil += "Potongan       : {}\n".format(self.hitung_potongan())
        hasil += "Total bayar    : {}".format(self.hitung_total_bayar())
        return hasil


nama_pelanggan = input("Nama pelanggan : ")
jenis_layanan = input("Jenis layanan : ")
harga = int(input("Harga per kg : "))
berat = float(input("Berat (kg) : "))

transaksi1 = Transaksi(nama_pelanggan, jenis_layanan, harga, berat)
print(transaksi1)
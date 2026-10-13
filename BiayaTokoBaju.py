# Program Biaya Toko Baju

class TokoBaju:
    # Atribut: jenis baju, jumlah, total harga
    def __init__(self, jenis_baju, jumlah):
        self.jenis_baju = jenis_baju
        self.jumlah = jumlah
        self.total_harga = 0

    # Menghitung total harga berdasarkan jenis baju dan jumlah
    def hitung_harga(self):
        if self.jenis_baju == "kaos":
            harga_satuan = 50000
        elif self.jenis_baju == "kemeja":
            harga_satuan = 80000
        elif self.jenis_baju == "celana":
            harga_satuan = 100000
        else:
            harga_satuan = 0

        total = harga_satuan * self.jumlah

        if self.jumlah >= 10:
            persen = 15
        elif self.jumlah >= 6:
            persen = 10
        elif self.jumlah >= 3:
            persen = 5
        else:
            persen = 0

        potongan = total * persen // 100
        self.total_harga = total - potongan
        return self.total_harga

    # Tampilan hasil
    def __str__(self):
        hasil = "===== STRUK TOKO BAJU =====\n"
        hasil += "Jenis baju  : {}\n".format(self.jenis_baju)
        hasil += "Jumlah      : {}\n".format(self.jumlah)
        hasil += "Total harga : {}".format(self.total_harga)
        return hasil


# ===== PROGRAM UTAMA =====
jenis_baju = input("Jenis baju (kaos/kemeja/celana) : ")
jumlah = int(input("Jumlah baju : "))

beli1 = TokoBaju(jenis_baju, jumlah)
beli1.hitung_harga()
print(beli1)
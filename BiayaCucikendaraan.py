# Program Biaya Cuci Kendaraan

class biayaCuci:
    # Atribut: jenis kendaraan, durasi layanan, total biaya
    def __init__(self, jenis_kendaraan, durasi):
        self.jenis_kendaraan = jenis_kendaraan
        self.durasi = durasi
        self.total_biaya = 0

    # Menghitung total biaya berdasarkan jenis kendaraan dan durasi
    def hitung_biaya(self):
        if self.jenis_kendaraan == "mobil":
            tarif_dasar = 30000
            tarif_tambahan = 10000
        elif self.jenis_kendaraan == "motor":
            tarif_dasar = 10000
            tarif_tambahan = 5000
        else:
            tarif_dasar = 0
            tarif_tambahan = 0

        if self.durasi <= 2:
            self.total_biaya = tarif_dasar
        else:
            jam_tambahan = self.durasi - 2
            self.total_biaya = tarif_dasar + (jam_tambahan * tarif_tambahan)

        return self.total_biaya

    # Tampilan hasil
    def __str__(self):
        hasil = "===== STRUK CUCI KENDARAAN =====\n"
        hasil += "Jenis kendaraan : {}\n".format(self.jenis_kendaraan)
        hasil += "Durasi layanan  : {} jam\n".format(self.durasi)
        hasil += "Total biaya     : {}".format(self.total_biaya)
        return hasil


# ===== PROGRAM UTAMA =====
jenis_kendaraan = input("Jenis kendaraan (mobil/motor) : ")
durasi = int(input("Durasi layanan (jam) : "))

cuci1 = biayaCuci(jenis_kendaraan, durasi)
cuci1.hitung_biaya()
print(cuci1)
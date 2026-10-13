'''
A. Method menentukan tarif atau harga (if/elif/else)

def tentukan_harga(self):
    if self.jenis == "mobil":
        self.harga = 30000
    elif self.jenis == "motor":
        self.harga = 10000
    else:
        self.harga = 0
    return self.harga




B. Method hitung total dasar
Harga x jumlah:

def hitung_total(self):
    self.total = self.harga * self.jumlah
    return self.total

    
Tarif dasar + biaya tambahan (seperti biayaCuci):

def hitung_total(self):
    if self.durasi <= 2:
        self.total = self.tarif_dasar
    else:
        self.total = self.tarif_dasar + (self.durasi - 2) * self.tarif_tambahan
    return self.total




C. Method diskon
Diskon berdasarkan jumlah barang:

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

    
Diskon berdasarkan total belanja:

def hitung_diskon(self):
    if self.total >= 500000:
        persen = 20
    elif self.total >= 200000:
        persen = 10
    else:
        persen = 0
    return persen


Diskon berdasarkan status member (and / or):

def hitung_diskon(self):
    if self.member == "ya" and self.total >= 100000:
        persen = 10
    elif self.member == "ya" or self.total >= 300000:
        persen = 5
    else:
        persen = 0
    return persen


Diskon tetap (nominal, bukan persen):

def hitung_diskon(self):
    if self.total >= 100000:
        return 10000
    else:
        return 0




D. Method potongan harga

def hitung_potongan(self):
    return self.total * self.hitung_diskon() // 100




E. Method biaya tambahan
Pajak:

def hitung_pajak(self):
    return self.total * 10 // 100


Biaya admin atau ongkir tetap:

def hitung_biaya_tambahan(self):
    if self.total >= 100000:
        return 0
    else:
        return 5000




F. Method total bayar
Dengan diskon:

def hitung_total_bayar(self):
    return self.total - self.hitung_potongan()


Dengan diskon dan pajak:

def hitung_total_bayar(self):
    setelah_diskon = self.total - self.hitung_potongan()
    return setelah_diskon + self.hitung_pajak()




G. Method uang kembalian dan cek pembayaran

def hitung_kembalian(self):
    return self.uang_bayar - self.hitung_total_bayar()

def cek_lunas(self):
    if self.uang_bayar >= self.hitung_total_bayar():
        return True
    else:
        return False




H. Method kategori atau status

def tentukan_kategori(self):
    if self.total >= 500000:
        return "Besar"
    elif self.total >= 200000:
        return "Sedang"
    else:
        return "Kecil"




I. Method validasi dengan raise (Pertemuan 4)

def cek_data(self):
    if self.jumlah < 0:
        raise ValueError("jumlah tidak boleh negatif")
    if self.harga < 0:
        raise ValueError("harga tidak boleh negatif")




J. Method mengubah data (seperti set_location di materi)
def set_data(self, jenis, jumlah):
    self.jenis = jenis
    self.jumlah = jumlah




K. __str__ (tampilan hasil)

def __str__(self):
    hasil = "===== STRUK =====\n"
    hasil += "Jenis        : {}\n".format(self.jenis)
    hasil += "Jumlah       : {}\n".format(self.jumlah)
    hasil += "Total        : {}\n".format(self.total)
    hasil += "Diskon       : {} persen\n".format(self.hitung_diskon())
    hasil += "Total bayar  : {}".format(self.hitung_total_bayar())
    return hasil




L. Operator overloading (Pertemuan 4, kalau soal membandingkan dua objek)

def __eq__(self, other):
    return self.total == other.total

def __lt__(self, other):
    return self.total < other.total

def __gt__(self, other):
    return self.total > other.total




M. Inheritance (Pertemuan 4, kalau ada class turunan)

class Member(Transaksi):
    def __init__(self, jenis, jumlah, kode_member):
        Transaksi.__init__(self, jenis, jumlah)
        self.kode_member = kode_member

    def hitung_diskon(self):
        return Transaksi.hitung_diskon(self) + 5




N. Beberapa transaksi sekaligus (loop Pertemuan 2)

jumlah_pelanggan = int(input("Jumlah pelanggan : "))
for i in range(jumlah_pelanggan):
    jenis = input("Jenis : ")
    jumlah = int(input("Jumlah : "))
    transaksi = Transaksi(jenis, jumlah)
    transaksi.hitung_total()
    print(transaksi)
'''
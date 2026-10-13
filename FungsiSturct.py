'''
toko baju:

# 1. di dalam class (__init__)
def __init__(self, nama_pelanggan, nama_baju, harga, jumlah):
    self.nama_baju = nama_baju

# 2. di dalam class (__str__)
hasil = "===== STRUK PEMBELIAN TOKO BAJU =====\n"
hasil += "Nama baju      : {}\n".format(self.nama_baju)
hasil += "Harga satuan   : {}\n".format(self.harga)
hasil += "Jumlah baju    : {}\n".format(self.jumlah)

# 3. di program utama
nama_baju = input("Nama baju : ")
harga = int(input("Harga satuan : "))
jumlah = int(input("Jumlah baju : "))
transaksi1 = Transaksi(nama_pelanggan, nama_baju, harga, jumlah)
'''



'''
Toko sepatu:

def __init__(self, nama_pelanggan, nama_sepatu, harga, jumlah):
    self.nama_sepatu = nama_sepatu

hasil = "===== STRUK PEMBELIAN TOKO SEPATU =====\n"
hasil += "Nama sepatu    : {}\n".format(self.nama_sepatu)
hasil += "Harga per pasang: {}\n".format(self.harga)
hasil += "Jumlah pasang   : {}\n".format(self.jumlah)

nama_sepatu = input("Nama sepatu : ")
harga = int(input("Harga per pasang : "))
jumlah = int(input("Jumlah pasang : "))
transaksi1 = Transaksi(nama_pelanggan, nama_sepatu, harga, jumlah)
'''



'''
Toko buku/alat tulis:

def __init__(self, nama_pelanggan, nama_buku, harga, jumlah):
    self.nama_buku = nama_buku

hasil = "===== STRUK PEMBELIAN TOKO BUKU =====\n"
hasil += "Nama buku      : {}\n".format(self.nama_buku)
hasil += "Harga per buku : {}\n".format(self.harga)
hasil += "Jumlah buku    : {}\n".format(self.jumlah)

nama_buku = input("Nama buku : ")
harga = int(input("Harga per buku : "))
jumlah = int(input("Jumlah buku : "))
transaksi1 = Transaksi(nama_pelanggan, nama_buku, harga, jumlah)
'''



'''
Toko elektronik:

def __init__(self, nama_pelanggan, nama_perangkat, harga, jumlah):
    self.nama_perangkat = nama_perangkat

hasil = "===== STRUK PEMBELIAN TOKO ELEKTRONIK =====\n"
hasil += "Nama perangkat : {}\n".format(self.nama_perangkat)
hasil += "Harga per unit : {}\n".format(self.harga)
hasil += "Jumlah unit    : {}\n".format(self.jumlah)

nama_perangkat = input("Nama perangkat : ")
harga = int(input("Harga per unit : "))
jumlah = int(input("Jumlah unit : "))
transaksi1 = Transaksi(nama_pelanggan, nama_perangkat, harga, jumlah)
'''



'''
Kafe/warung makan:

python
def __init__(self, nama_pelanggan, nama_menu, harga, jumlah):
    self.nama_menu = nama_menu

hasil = "===== STRUK PEMBAYARAN KAFE =====\n"
hasil += "Nama menu      : {}\n".format(self.nama_menu)
hasil += "Harga per porsi: {}\n".format(self.harga)
hasil += "Jumlah porsi   : {}\n".format(self.jumlah)

nama_menu = input("Nama menu : ")
harga = int(input("Harga per porsi : "))
jumlah = int(input("Jumlah porsi : "))
transaksi1 = Transaksi(nama_pelanggan, nama_menu, harga, jumlah)
'''



'''
Cuci sepatu:

def __init__(self, nama_pelanggan, jenis_cucian, harga, jumlah):
    self.jenis_cucian = jenis_cucian

hasil = "===== STRUK CUCI SEPATU =====\n"
hasil += "Jenis cucian   : {}\n".format(self.jenis_cucian)
hasil += "Harga per pasang: {}\n".format(self.harga)
hasil += "Jumlah pasang   : {}\n".format(self.jumlah)

jenis_cucian = input("Jenis cucian : ")
harga = int(input("Harga per pasang : "))
jumlah = int(input("Jumlah pasang : "))
transaksi1 = Transaksi(nama_pelanggan, jenis_cucian, harga, jumlah)
'''



'''
Fotokopi/percetakan:

def __init__(self, nama_pelanggan, jenis_cetakan, harga, jumlah):
    self.jenis_cetakan = jenis_cetakan

hasil = "===== STRUK PERCETAKAN =====\n"
hasil += "Jenis cetakan  : {}\n".format(self.jenis_cetakan)
hasil += "Harga per lembar: {}\n".format(self.harga)
hasil += "Jumlah lembar   : {}\n".format(self.jumlah)

jenis_cetakan = input("Jenis cetakan : ")
harga = int(input("Harga per lembar : "))
jumlah = int(input("Jumlah lembar : "))
transaksi1 = Transaksi(nama_pelanggan, jenis_cetakan, harga, jumlah)
'''



'''
Tiket bioskop/konser

def __init__(self, nama_pelanggan, nama_acara, harga, jumlah):
    self.nama_acara = nama_acara

hasil = "===== STRUK PEMBELIAN TIKET =====\n"
hasil += "Nama acara     : {}\n".format(self.nama_acara)
hasil += "Harga per tiket: {}\n".format(self.harga)
hasil += "Jumlah tiket   : {}\n".format(self.jumlah)

nama_acara = input("Nama film/acara : ")
harga = int(input("Harga per tiket : "))
jumlah = int(input("Jumlah tiket : "))
transaksi1 = Transaksi(nama_pelanggan, nama_acara, harga, jumlah)
'''


'''
Rental (motor/kamera):

python
def __init__(self, nama_pelanggan, nama_barang_sewa, harga, jumlah):
    self.nama_barang_sewa = nama_barang_sewa

hasil = "===== STRUK PENYEWAAN =====\n"
hasil += "Barang sewa    : {}\n".format(self.nama_barang_sewa)
hasil += "Harga per hari : {}\n".format(self.harga)
hasil += "Jumlah hari    : {}\n".format(self.jumlah)

nama_barang_sewa = input("Nama barang sewa : ")
harga = int(input("Harga per hari : "))
jumlah = int(input("Jumlah hari : "))
transaksi1 = Transaksi(nama_pelanggan, nama_barang_sewa, harga, jumlah)
'''
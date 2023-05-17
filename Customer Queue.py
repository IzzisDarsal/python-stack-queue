class TransaksiPelanggan:
    def __init__(self, nama, jenis_transaksi):
        self.nama = nama
        self.jenis_transaksi = jenis_transaksi

class AntreanTransaksi:
    def __init__(self):
        self.antrean = []

    def kosong(self):
        return len(self.antrean) == 0

    def tambah_transaksi(self, transaksi):
        self.antrean.append(transaksi)
        print(f"Transaksi {transaksi.jenis_transaksi} oleh {transaksi.nama} berhasil ditambahkan ke dalam antrean.")

    def hapus_transaksi_terlayani(self):
        if self.kosong():
            print("Antrean kosong. Tidak ada transaksi yang dapat dihapus.")
            return None
        else:
            transaksi = self.antrean.pop(0)
            print(f"Transaksi {transaksi.jenis_transaksi} oleh {transaksi.nama} berhasil dilayani.")
            return transaksi

    def transaksi_berikutnya(self):
        if self.kosong():
            print("Antrean kosong. Tidak ada transaksi yang akan dilayani.")
        else:
            transaksi = self.antrean[0]
            print(f"Transaksi berikutnya yang akan dilayani adalah {transaksi.jenis_transaksi} oleh {transaksi.nama}.")


antrean_transaksi = AntreanTransaksi()

while True:
    print("\nAntrean transaksi saat ini:")
    for i, transaksi in enumerate(antrean_transaksi.antrean, start=1):
        print(f"{i}. {transaksi.jenis_transaksi} oleh {transaksi.nama}")

    print("Menu:")
    print("1. Tambah Transaksi")
    print("2. Layani Transaksi Berikutnya")
    print("3. Hapus Transaksi yang Telah Dilayani")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        nama = input("Masukkan nama pelanggan: ")
        jenis_transaksi = input("Masukkan jenis transaksi: ")
        transaksi = TransaksiPelanggan(nama, jenis_transaksi)
        antrean_transaksi.tambah_transaksi(transaksi)
    elif pilihan == "2":
        antrean_transaksi.transaksi_berikutnya()
    elif pilihan == "3":
        antrean_transaksi.hapus_transaksi_terlayani()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

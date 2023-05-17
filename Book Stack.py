class TumpukanBuku:
    def __init__(self):
        self.tumpukan = []

    def kosong(self):
        return len(self.tumpukan) == 0

    def tambah_buku(self, judul_buku, pengarang):
        buku = {"Judul Buku": judul_buku, "Pengarang": pengarang}
        self.tumpukan.append(buku)
        print(f"{judul_buku} berhasil ditambahkan ke dalam tumpukan.")

    def hapus_buku_terakhir(self):
        if self.kosong():
            print("Tumpukan kosong. Tidak ada buku yang dapat dihapus.")
        else:
            buku = self.tumpukan.pop()
            print(f"{buku['Judul Buku']} berhasil dihapus dari tumpukan.")

    def buku_teratas(self):
        if self.kosong():
            print("Tumpukan kosong. Tidak ada buku yang dapat ditampilkan.")
        else:
            buku = self.tumpukan[-1]
            print(f"Buku teratas dalam tumpukan adalah '{buku['Judul Buku']}' oleh {buku['Pengarang']}.")


tumpukan_buku = TumpukanBuku()

while True:
    print("\nTumpukan buku saat ini:", tumpukan_buku.tumpukan)
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        judul_buku = input("Masukkan judul buku: ")
        pengarang = input("Masukkan nama pengarang: ")
        tumpukan_buku.tambah_buku(judul_buku, pengarang)
    elif pilihan == "2":
        tumpukan_buku.hapus_buku_terakhir()
    elif pilihan == "3":
        tumpukan_buku.buku_teratas()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

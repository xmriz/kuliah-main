# ============================ F14 ========================================
def help():
    # Menampilkan keyword-keyword yang tersedia ke layar
    
    # I.S. sembarang
    # F.S. tercetak list keyword help ke layar
    
    # KAMUS LOKAL

    # ALGORITMA
    print("""
============================================================ HELP ============================================================
Berikut merupakan keyword yang dapat digunakan beserta fungsi dan aksesnya
Ketikkan keyword di bawah ini untuk melakukan fungsi yang diinginkan

| \033[1mregister\033[0m              | melakukan registrasi user baru                                                         \033[33m(Akses: Admin)\033[0m
| \033[1mlogin\033[0m                 | melakukan login ke dalam sistem                                                        \033[33m(Akses: Admin/User)\033[0m
| \033[1mtambah_game\033[0m           | menambah game yang dijual pada toko                                                    \033[33m(Akses: Admin)\033[0m
| \033[1mubah_game\033[0m             | mengubah game pada toko                                                                \033[33m(Akses: Admin)\033[0m
| \033[1mubah_stok\033[0m             | mengubah stok sebuah game pada toko                                                    \033[33m(Akses: Admin)\033[0m
| \033[1mlist_game_toko\033[0m        | melihat list game yang ada di toko                                                     \033[33m(Akses: Admin/User)\033[0m
| \033[1mbuy_game\033[0m              | membeli game dan memasukkan ke dalam list game user                                    \033[33m(Akses: User)\033[0m
| \033[1msearch_my_game\033[0m        | mencari game yang dimiliki berdasarkan ID dan tahun rilis                              \033[33m(Akses: User)\033[0m
| \033[1msearch_game_at_store\033[0m  | mencari game di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis       \033[33m(Akses: Admin/User)\033[0m
| \033[1mtopup\033[0m                 | menambah saldo kepada user                                                             \033[33m(Akses: Admin)\033[0m
| \033[1mriwayat\033[0m               | melihat riwayat pembelian game                                                         \033[33m(Akses: User)\033[0m
| \033[1msave\033[0m                  | menyimpan data setelah dilakukan perubahan                                             \033[33m(Akses: Admin/User)\033[0m
| \033[1mhelp\033[0m                  | memberikan panduan penggunaan sistem                                                   \033[33m(Tidak perlu login)\033[0m
| \033[1mexit\033[0m                  | keluar dari aplikasi                                                                   \033[33m(Tidak perlu login)\033[0m
          """)


help()
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

graph = {
    "Mikhub"    : {"Boyolali": 30, "Solo": 70, "Semarang": 90, "Yogyakarta": 110},
    "Boyolali"  : {"Mikhub": 30, "Solo": 30, "Semarang": 100},
    "Solo"      : {"Mikhub": 70, "Boyolali": 30, "Semarang": 80, "Yogyakarta": 60},
    "Semarang"  : {"Mikhub": 90, "Boyolali": 100, "Solo": 80, "Yogyakarta": 120},
    "Yogyakarta": {"Mikhub": 110, "Solo": 60, "Semarang": 120}
}

def inputan_hub_kota_baru():
    while True:
        clear()
        print('*' + '=' * 55 + '*')
        print('*                Menu Input Hub Kota Baru               *')
        print('*' + '=' * 55 + '*')

        kota = str(input("\n Masukkan Nama Kota Yang Ingin Ditambahkan: ").strip().title())
        print('\n*' + '=' * 55 + '*')

        if kota == "":
            print("\n Nama kota tidak boleh kosong. ")
            input(" Tekan Enter untuk melanjutkan...")
            continue

        elif not all(c.isalpha() or c.isspace() for c in kota):
            print("\n Nama kota hanya boleh berisi huruf dan spasi. ")
            input(" Tekan Enter untuk melanjutkan...")
            continue

        if kota in graph:
            print(f" Hub untuk kota '{kota}' sudah terdaftar.")
            return

        graph[kota] = {}
        print('*                     SELAMAT!!                         *')
        print(f" Hub untuk kota '{kota}' sudah berhasil ditambahkan. ")
        break

def inputan_rute_antar_kota():
    if len(graph) < 2:
        clear()
        print('*' + '=' * 83 + '*')
        print('*                             Menu Input Rute Antar-Kota                            *')
        print('*' + '=' * 83 + '*')

        print("Minimal harus terdapat 2 hub kota untuk membuat rute antar-kota.")
        return    

    clear()
    print('*' + '=' * 83 + '*')
    print('*                             Menu Input Rute Antar-Kota                            *')
    print('*' + '=' * 83 + '*')

    print("Daftar Hub Antar Kota:")
    for kota in graph:
        print(f"- {kota}")
    print('*' + '=' * 83 + '*')

    while True:
        kota_asal = input(f"{'Masukkan nama kota asal':<40}: ").strip().title()
        if not all(c.isalpha() or c.isspace() for c in kota_asal):
            print('*' + '=' * 83 + '*')
            print("Nama kota hanya boleh berisi huruf dan spasi.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue

        if kota_asal == "":
            print('*' + '=' * 83 + '*')
            print("Nama kota tidak boleh kosong.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue

        if kota_asal not in graph:
            print('*' + '=' * 83 + '*')
            print(f"Hub untuk kota '{kota_asal}' belum terdaftar.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue
        break

    while True:
        clear()
        print('*' + '=' * 83 + '*')
        print('*                             Menu Input Rute Antar-Kota                            *')
        print('*' + '=' * 83 + '*')

        print("Daftar Hub Antar Kota:")
        for kota in graph:
            print(f"- {kota}")

        print('*' + '=' * 83 + '*')
        print(f" Kota asal: {kota_asal}")
        print('*' + '=' * 83 + '*')

        kota_tujuan = input(f"{' Masukkan nama kota tujuan':<41}: ").strip().title()
        if not all(c.isalpha() or c.isspace() for c in kota_tujuan):
            print('*' + '=' * 83 + '*')
            print("Nama kota hanya boleh berisi huruf dan spasi.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue

        if kota_tujuan == "":
            print('*' + '=' * 83 + '*')
            print("Nama kota tidak boleh kosong.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue

        if kota_tujuan not in graph:
            print('*' + '=' * 83 + '*')
            print(f'Kota tujuan "{kota_tujuan}" belum terdaftar.')
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue

        if kota_asal == kota_tujuan:
            print('*' + '=' * 83 + '*')
            print("Kota asal dan kota tujuan tidak boleh sama.")
            print('*' + '=' * 83 + '*')
            input('Tekan Enter untuk melanjutkan...')
            continue
        
        if kota_tujuan in graph[kota_asal]:
            print('*' + '=' * 83 + '*')
            print(f"Rute dari kota '{kota_asal}' ke kota '{kota_tujuan}' sudah terdaftar dengan jarak {graph[kota_asal][kota_tujuan]} KM.")
            return
        break

    while True:
        clear()
        print('*' + '=' * 83 + '*')
        print('*                             Menu Input Rute Antar-Kota                            *')
        print('*' + '=' * 83 + '*')

        print(f' Kota asal: {kota_asal}')
        print('*' + '=' * 83 + '*')
        print(f' Kota tujuan: {kota_tujuan}')
        print('*' + '=' * 83 + '*')

        try:
            jarak_tempuh = float(input(" Masukkan jarak tempuh (dalam Kilo Meter): "))
            if jarak_tempuh <= 0:
                print('Jarak tempuh harus lebih besar dari 0.')
                input('Tekan Enter untuk melanjutkan...')
                continue
            break
        except ValueError:
            print('jarak tempuh harus berupa angka.')
            input('Tekan Enter untuk melanjutkan...')


    graph[kota_asal][kota_tujuan] = jarak_tempuh
    graph[kota_tujuan][kota_asal] = jarak_tempuh

    print('*' + '=' * 83 + '*')
    print(f"Rute dari '{kota_asal}' ke '{kota_tujuan}' dengan jarak {jarak_tempuh} KM sudah berhasil ditambahkan.")
    print('*' + '=' * 83 + '*')
    return

class Noderesi:
    def __init__(self, No_Resi, Nama_Pengirim, Kota_Asal, Kota_Tujuan, Berat_Paket, Total_Biaya_Kirim):
        self.nomor_resi = No_Resi
        self.nama_pengirim = Nama_Pengirim
        self.kota_asal = Kota_Asal
        self.kota_tujuan = Kota_Tujuan
        self.berat_barang = Berat_Paket
        self.total_biaya_kirim = Total_Biaya_Kirim
        self.kiri = None
        self.kanan = None

class ResiBST:
    def __init__(self):
        self.root = None

def insert_bst(node, No_Resi, Nama_Pengirim, Kota_Asal, Kota_Tujuan, Berat_Paket, Total_Biaya_Kirim):
    if node is None:
        return Noderesi(No_Resi, Nama_Pengirim, Kota_Asal, Kota_Tujuan, Berat_Paket, Total_Biaya_Kirim)
    if No_Resi < node.nomor_resi:
        node.kiri = insert_bst(node.kiri, No_Resi, Nama_Pengirim, Kota_Asal, Kota_Tujuan, Berat_Paket, Total_Biaya_Kirim)
    elif No_Resi > node.nomor_resi:
        node.kanan = insert_bst(node.kanan, No_Resi, Nama_Pengirim, Kota_Asal, Kota_Tujuan, Berat_Paket, Total_Biaya_Kirim)
    return node

bst_resi = ResiBST()
data_awal = [
        (1034, "Mikha", "Solo", "Yogyakarta", 2.5),
        (1231, "Khael", "Mikhub", "Solo", 1.0),
        (1534, "El", "Yogyakarta", "Semarang", 3.0),
        (1004, "Awan", "Solo", "Mikhub", 0.5)
]

for no, nama, asal, tujuan, berat in data_awal:
    jarak = graph[asal][tujuan]
    biaya_kirim = (jarak * 2000) + (berat * 5000)
    bst_resi.root = insert_bst(bst_resi.root, no, nama, asal, tujuan, berat, biaya_kirim)

def inorder(node, hasil):
    if node is None:
        return
    inorder(node.kiri, hasil)
    hasil.append(node)
    inorder(node.kanan, hasil)

def cek_duplikat(node, no_resi):
    if node is None:
        return False
    if node.nomor_resi == no_resi:
        return True
    elif no_resi < node.nomor_resi:
        return cek_duplikat(node.kiri, no_resi)
    else:
        return cek_duplikat(node.kanan, no_resi)

def input_resi_pengiriman_baru():
    while True:
        clear()
        print('*' + '=' * 59 + '*')
        print('*             Menu Input Resi Pengiriman Baru               *')
        print('*' + '=' * 59 + '*')

        try:
            no_resi = int(input(f"{'Masukkan nomor resi (4 digit, diawali dengan angka 1): ':<2}").strip())

            if len(str(no_resi)) != 4:
                print("Nomor resi harus terdiri dari 4 digit angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not str(no_resi)[0] == '1':
                print("Nomor resi harus diawali dengan angka '1'.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if cek_duplikat(bst_resi.root, no_resi):
                print(f"Nomor resi '{no_resi}' sudah terdaftar. Silakan masukkan nomor resi yang berbeda.")
                input("Tekan Enter untuk melanjutkan...")
                continue
        except ValueError:
            print("Nomor resi harus berupa angka dan tidak boleh kosong.")
            input("Tekan Enter untuk melanjutkan...")
            continue

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*             Menu Input Resi Pengiriman Baru               *')
            print('*' + '=' * 59 + '*')

            print(f"{' Nomor Resi yang baru dibuat':<33}: {no_resi}")

            nama_pengirim = str(input(f"{' Masukkan nama pengirim':<33}: ").strip().title())
            if nama_pengirim == "":
                print("Nama pengirim harus diisi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if nama_pengirim.isdigit():
                print("Nama pengirim tidak boleh berupa angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not all(c.isalpha() or c.isspace() for c in nama_pengirim):
                print("Nama pengirim hanya boleh berisi huruf dan spasi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*             Menu Input Resi Pengiriman Baru               *')
            print('*' + '=' * 59 + '*')

            print(f"{' Nomor Resi yang baru dibuat':<33}: {no_resi}")
            print(f"{' Nama Pengirim':<33}: {nama_pengirim}")

            kota_asal = input(f"{' Masukkan kota asal':<33}: ").strip().title()
            if kota_asal == "":
                print("Kota asal harus diisi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if kota_asal.isdigit():
                print("Kota asal tidak boleh berupa angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not all(c.isalpha() or c.isspace() for c in kota_asal):
                print("Kota asal hanya boleh berisi huruf dan spasi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if kota_asal not in graph:
                print(f"Kota asal '{kota_asal}' belum terdaftar dalam jaringan hub.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*             Menu Input Resi Pengiriman Baru               *')
            print('*' + '=' * 59 + '*')

            print(f"{' Nomor Resi yang baru dibuat':<33}: {no_resi}")
            print(f"{' Nama Pengirim':<33}: {nama_pengirim}")
            print(f"{' Kota Asal':<33}: {kota_asal}")

            kota_tujuan = input(f"{' Masukkan kota tujuan':<33}: ").strip().title()
            if kota_tujuan == "":
                print("Kota tujuan harus diisi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if kota_tujuan.isdigit():
                print("Kota tujuan tidak boleh berupa angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not all(c.isalpha() or c.isspace() for c in kota_tujuan):
                print("Kota tujuan hanya boleh berisi huruf dan spasi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if kota_tujuan not in graph[kota_asal]:
                print(f"Rute pengiriman belum tersedia dalam jaringan!")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*             Menu Input Resi Pengiriman Baru               *')
            print('*' + '=' * 59 + '*')
            print(f"{' Nomor Resi yang baru dibuat':<33}: {no_resi}")
            print(f"{' Nama Pengirim':<33}: {nama_pengirim}")
            print(f"{' Kota Asal':<33}: {kota_asal}")
            print(f"{' Kota Tujuan':<33}: {kota_tujuan}")

            Jarak_Rute = graph[kota_asal][kota_tujuan]

            try:
                Berat_Paket = float(input(f"{' Masukkan berat paket (dalam Kg) ':<33}: ").strip())
                if Berat_Paket <= 0:
                    print("Berat paket harus lebih besar dari 0.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

            except ValueError:
                print("Berat paket harus berupa angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        biaya_kirim = (Jarak_Rute * 2000) + (Berat_Paket * 5000)
        bst_resi.root = insert_bst(bst_resi.root, no_resi, nama_pengirim, kota_asal, kota_tujuan, Berat_Paket, biaya_kirim)

        clear()
        print('*' + '=' * 59 + '*')
        print('*     Input Resi Berhasil     *')
        print('*' + '=' * 59 + '*')

        print(f"{' Nomor Resi yang baru dibuat':<33}: {no_resi}")
        print(f"{' Nama Pengirim':<33}: {nama_pengirim}")
        print(f"{' Kota Asal':<33}: {kota_asal}")
        print(f"{' Kota Tujuan':<33}: {kota_tujuan}")
        print(f"{' Berat Paket (Kg)':<33}: {Berat_Paket:.2f}")
        print('*' + '=' * 59 + '*')

        print(f"{' Resi pengiriman baru dengan jarak rute (KM)':<33}: {Jarak_Rute:.2f}")
        print(f"{' Total biaya kirim untuk resi ini adalah':<33}: Rp {biaya_kirim:,.0f}")
        print('*' + '=' * 59 + '*')

        ulang = input("\nApakah ingin melakukan input resi lagi? (Y/N): ").strip().upper()
        if ulang != 'Y' or ulang == "":
            break

def lihat_data_resi():
    clear()
    print('*' + '=' * 105 + '*')
    print('*                                Menu Lihat Seluruh Data Resi Terdaftar                                   *')
    print('*' + '=' * 105 + '*')

    if bst_resi.root is None:
        print("Belum ada data resi yang terdaftar.")
        return

    hasil = []
    inorder(bst_resi.root, hasil)

    print(f"* {'No Resi':<10} {'Nama Pengirim':<18} {'Kota Asal':<15} {'Kota Tujuan':<15} {'Berat Paket (Kg)':<18} {'Total Biaya Kirim (Rp)':<23}*")
    print('*' + '=' * 105 + '*')

    for node in hasil:
        print(f"* {node.nomor_resi:<10} {node.nama_pengirim:<18} {node.kota_asal:<15} {node.kota_tujuan:<15} {node.berat_barang:<18.2f} {node.total_biaya_kirim:<23,.0f}*")

def quick_sort_resi(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    kiri = [x for x in arr if x.total_biaya_kirim > pivot.total_biaya_kirim]
    tengah = [x for x in arr if x.total_biaya_kirim == pivot.total_biaya_kirim]
    kanan = [x for x in arr if x.total_biaya_kirim < pivot.total_biaya_kirim]

    return quick_sort_resi(kiri) + tengah + quick_sort_resi(kanan)

def urutkan_resi_biaya_terbesar():
    clear()
    print('*' + '=' * 106 + '*')
    print('*                        Menu Urutkan Transaksi Resi Berdasarkan Biaya Terbesar                            *')
    print('*' + '=' * 106 + '*')

    if bst_resi.root is None:
        print("Belum ada data resi yang terdaftar.")
        return
    
    list_resi = []
    inorder(bst_resi.root, list_resi)
    resi_terurut = quick_sort_resi(list_resi)

    print(f"*{' No Resi':<12} {'Nama Pengirim':<18} {'Kota Asal':<15} {'Kota Tujuan':<15} {'Berat Paket (Kg)':<18} {'Total Biaya Kirim (Rp)':<23}*")
    print('*'+ '=' * 106 + '*')

    for node in resi_terurut:
        print(f"* {node.nomor_resi:<12}{node.nama_pengirim:<18} {node.kota_asal:<15} {node.kota_tujuan:<15} {node.berat_barang:<18.2f} {node.total_biaya_kirim:<23,.0f}*")

kurir = [
    {"ID Kurir": 2001, "Nama Kurir": "Budi", "Jenis Kendaraan": "Motor"},
    {"ID Kurir": 2002, "Nama Kurir": "Siti", "Jenis Kendaraan": "Mobil"},
]

def input_data_kurir():
    while True:
        clear()
        print('*' + '=' * 59 + '*')
        print('*                    Menu Input Data Kurir                    *')
        print('*' + '=' * 59 + '*')

        try: 
            id_kurir = int(input("Masukkan ID Kurir: ").strip())

            if len(str(id_kurir)) != 4:
                print("ID Kurir harus terdiri dari 4 buah angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            elif any(k["ID Kurir"] == id_kurir for k in kurir):
                print(f"ID Kurir '{id_kurir}' sudah terdaftar. Silakan masukkan ID yang berbeda.")
                input("Tekan Enter untuk melanjutkan...")
                continue

        except ValueError:
            print("ID Kurir harus berupa angka dan tidak boleh kosong.")
            input("Tekan Enter untuk melanjutkan...")
            continue        

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*                    Menu Input Data Kurir                    *')
            print('*' + '=' * 59 + '*')

            print(f"{'ID Kurir':<44}: {id_kurir}")

            nama_kurir = input("Masukkan Nama Kurir: ").strip().title()
            if nama_kurir == "":
                print("Nama Kurir tidak boleh kosong.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if nama_kurir.isdigit():
                print("Nama Kurir tidak boleh berupa angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not all(c.isalpha() or c.isspace() for c in nama_kurir):
                print("Nama kurir hanya boleh berisi huruf dan spasi.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        while True:
            clear()
            print('*' + '=' * 59 + '*')
            print('*                    Menu Input Data Kurir                    *')
            print('*' + '=' * 59 + '*')

            print(f"{'ID Kurir':<44}: {id_kurir}")
            print(f"{'Nama Kurir':<44}: {nama_kurir}")

            jenis_kendaraan = input("Masukkan Jenis Kendaraan (Motor/Mobil/Truck): ").strip().title()
            if jenis_kendaraan not in ["Motor", "Mobil", "Truck"]:
                print("Jenis kendaraan harus berupa 'Motor', 'Mobil', atau 'Truck'.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break

        kurir.append({"ID Kurir": id_kurir, "Nama Kurir": nama_kurir, "Jenis Kendaraan": jenis_kendaraan})

        print('\n*' + '=' * 59 + '*')
        print(f"               Data kurir Berhasil Dinputkan          ")
        print('*' + '=' * 59 + '*')

        ulang = input("\nApakah Anda ingin memasukkan data kurir baru lagi? (Y/N): ").strip().upper()
        if ulang != 'Y' or ulang == "":
            break

Petugas_Manifest = {}

def plotting_penugasan_manifest():
    clear()

    print('*' + '=' * 59 + '*')
    print('*         Menu Plotting Penugasan Manifest              *')
    print('*' + '=' * 59 + '*')

    if not kurir:
        print("Belum ada data kurir yang terdaftar.")
        input("Tekan Enter untuk melanjutkan....")
        return

    while True:
        clear()
        print('*' + '=' * 59 + '*')
        print('*            Menu Plotting Penugasan Manifest              *')
        print('*' + '=' * 59 + '*')
        print("Daftar Kurir:")
        for k in kurir:
            print(f"- ID: {k['ID Kurir']}, Nama: {k['Nama Kurir']}, Kendaraan: {k['Jenis Kendaraan']}")

        try:
            id_kurir = int(input("Masukkan ID Kurir yang akan ditugaskan: ").strip())
            kurir_terpilih = next((k for k in kurir if k["ID Kurir"] == id_kurir), None)
            if kurir_terpilih is None:
                print(f"ID Kurir '{id_kurir}' tidak ditemukan. Silakan masukkan ID yang valid.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            break
        except ValueError:
            print("ID Kurir harus berupa angka dan tidak boleh kosong.")
            input("Tekan Enter untuk melanjutkan...")
            continue    
    
    if bst_resi.root is None:
        print("Belum ada data resi yang terdaftar.")
        return

    if id_kurir not in Petugas_Manifest:
        Petugas_Manifest[id_kurir] = []
    
    while True:
        clear()
        print('*' + '=' * 59 + '*')
        print('*         Menu Plotting Penugasan Manifest              *')
        print('*' + '=' * 59 + '*')
        
        print(f"{'Kurir Terpilih':<22}: {id_kurir}")

        hasil = []
        inorder(bst_resi.root, hasil)
        print("Daftar Resi Pengiriman:")
        for node in hasil:
            sudah = any(node.nomor_resi in resi_list for resi_list in Petugas_Manifest.values())
            status = "Sudah Ditugaskan" if sudah else "Belum Ditugaskan"
            print(f"-{node.nomor_resi} {('|'):>5} {node.nama_pengirim} | {status}")
        print('*' + '=' * 59 + '*')

        try:
            no_resi = int(input("Masukkan nomor resi yang akan ditugaskan ke kurir ini: ").strip())

            if len(str(no_resi)) != 4:
                print(f"Nomor resi harus terdiri dari 4 digit angka.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            if not str(no_resi)[0] == '1':
                print(f"Nomor resi harus diawali dengan angka '1'.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            elif any(no_resi in resi_list for resi_list in Petugas_Manifest.values()):
                print(f"Nomor resi '{no_resi}' sudah ditugaskan ke kurir lain. Silakan pilih nomor resi yang belum ditugaskan.")
                input("Tekan Enter untuk melanjutkan...")
                continue
            elif not cek_duplikat(bst_resi.root, no_resi):
                print(f"Nomor resi '{no_resi}' tidak ditemukan. Silakan masukkan nomor resi yang valid.")
                input("Tekan Enter untuk melanjutkan...")
                continue

        except ValueError:
            print("Nomor resi harus berupa angka dan tidak boleh kosong.")
            input("Tekan Enter untuk melanjutkan...")
            continue

        Petugas_Manifest[id_kurir].append(no_resi)
        print(f"Resi nomor '{no_resi}' berhasil ditugaskan ke kurir ID '{id_kurir}'.")
        print('*' + '=' * 59 + '*')

        ulang = input("\nApakah Anda ingin menugaskan resi lain ke kurir ini? (Y/N): ").strip().upper()
        if ulang != 'Y' or ulang == "":
            break

def tampil_manifest_dan_aturan_bonus_insentif():
    clear()

    print('*' + '=' * 59 + '*')
    print('*      Menu Tampil Manifest & Aturan Bonus Insentif         *')
    print('*' + '=' * 59 + '*')

    if not kurir:
        print("Belum ada data kurir yang terdaftar.")
        return
    print("Daftar Kurir:")
    for k in kurir:
        no_resi_yg_ditugaskan = Petugas_Manifest.get(k["ID Kurir"], [])
        jumlah = len(no_resi_yg_ditugaskan)
        
        if jumlah == 0:
            lencana, bonus = "Kurir Santai", 0
        elif jumlah <= 3:
            lencana, bonus = "Kurir Reguler", 25000
        elif jumlah <= 6:
            lencana, bonus = "Kurir Produktif", 60000     
        else:
            lencana, bonus = "Kurir Elite", 120000

        print(f"\nID Kurir                : {k['ID Kurir']}")
        print(f"Nama Kurir              : {k['Nama Kurir']}")
        print(f"Jenis Kendaraan         : {k['Jenis Kendaraan']}")
        print(f"Jumlah Paket            : {jumlah}")
        print(f"Lencana Kurir           : {lencana}")
        print(f"Bonus Insentif Tambahan : Rp {bonus:,}")
        print('*' + '=' * 59 + '*')

        if jumlah == 0:
            print("TIdak ada paket yang dibawa")
        
        else:
            print(f" {'No Resi':<10} {'Nama Pengirim':<20} {'Kota Asal':<10} {'Kota Tujuan':<15} {'Biaya':<15}")
            for no_resi in no_resi_yg_ditugaskan:
                node = bst_resi.root
                while node is not None:
                    if no_resi == node.nomor_resi:
                        print(f" {node.nomor_resi:<10} {node.nama_pengirim:<20} {node.kota_asal:<10} {node.kota_tujuan:<15} Rp {node.total_biaya_kirim:<15,.0f}")
                        break
                    elif no_resi < node.nomor_resi:
                        node = node.kiri
                    else:
                        node = node.kanan
        print('*' + '=' * 59 + '*')
    input("\nTekan Enter untuk melanjutkan...")

def menu_kelola_jaringan_hub():
    while True:
        clear()

        print('*============================================*')
        print('* Menu Kelola Jaringan Hub dan Rute Logistik *')
        print('*============================================*')
        print('*                                            *')
        print('*    1.1) Input Hub Kota Baru                *')
        print('*    1.2) Input Rute Antar-Kota              *')
        print('*    1.3) Kembali Ke Menu Utama              *')
        print('*                                            *')
        print('*============================================*')

        pilihan = input("Pilih Menu: ").strip().replace(")", "")
        
        if pilihan == "1.1":
            inputan_hub_kota_baru()
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "1.2":
            inputan_rute_antar_kota()
            input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "1.3":
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

def menu_kelola_administrasi():
    while True:
        clear()

        print('*===========================================================*')
        print('*         Menu Kelola Administrasi Resi Pengiriman          *')
        print('*===========================================================*')
        print('*                                                           *')
        print('*    2.1) Input Resi Pengiriman Baru                        *')
        print('*    2.2) Lihat Seluruh Data Resi Terdaftar                 *')
        print('*    2.3) Urutkan Transaksi Resi Berdasarkan Biaya Terbesar *')
        print('*    2.4) Kembali Ke Menu Utama                             *')
        print('*                                                           *')
        print('*===========================================================*')

        pilihan = input("Pilih Menu: ").strip().replace(")", "") 

        if pilihan == "2.1":
            input_resi_pengiriman_baru()

        elif pilihan == "2.2":
            lihat_data_resi()
            input("Tekan Enter untuk kembali ke sub-menu...")

        elif pilihan == "2.3":
            urutkan_resi_biaya_terbesar()
            input("Tekan Enter untuk kembali ke sub-menu...")

        elif pilihan == "2.4":
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

def kelola_kurir_dan_manifest_pengantaran():
    while True:
        clear()

        print('*===========================================================*')
        print('*         Menu Kelola Kurir dan Manifest Pengantaran        *')
        print('*===========================================================*')
        print('*                                                           *')
        print('*    3.1) Input Data Kurir                                  *')
        print('*    3.2) Plotting Penugasan Manifest                       *')
        print('*    3.3) Tampil Manifest & Aturan Bonus Insentif           *')
        print('*    3.4) Kembali Ke Menu Utama                             *')
        print('*                                                           *')
        print('*===========================================================*')

        pilihan = input("Pilih Menu: ").strip().replace(")", "") 

        if pilihan == "3.1":
            input_data_kurir()

        elif pilihan == "3.2":
            plotting_penugasan_manifest()

        elif pilihan == "3.3":
            tampil_manifest_dan_aturan_bonus_insentif()
            input("Tekan Enter untuk kembali ke sub-menu...")

        elif pilihan == "3.4":
            print("Kembali ke menu utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

while True:
    clear()
    print('*======== Selamat Datang Di Menu Silog ==========*')
    print('*====== Silahkan pilih menu yang tersedia =======*')
    print('*================================================*')
    print(' *                                               *')
    print(' *   1. Kelola Jaringan Hub dan Rute Logistik    *')
    print(' *   2. Kelola Administrasi Resi Pengiriman      *')
    print(' *   3. Kelola Kurir dan Manifest Pengantaran    *')
    print(' *   0. Exit Program                             *')
    print(' *                                               *')
    print('*================================================*')

    try:
        pilihan = int(input('Masukkan pilihan Anda (1/2/3/0): '))

    except ValueError:
        print("Input tidak valid. Silakan masukkan angka 1, 2, 3, atau 0.")
        input("Tekan Enter untuk melanjutkan...")
        continue

    if pilihan == 1:
        menu_kelola_jaringan_hub()
    elif pilihan == 2:
        menu_kelola_administrasi()
    elif pilihan == 3:
        kelola_kurir_dan_manifest_pengantaran()
    elif pilihan == 0:
        print('\nTerima kasih atas kerja samanya. Sampai jumpa kembali !!')
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1, 2, 3, atau 0.")
        input("Tekan Enter untuk melanjutkan...")

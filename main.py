from colorama import init, Style
from colorama import init, Fore, Style

init()

data_pengguna = {}
data_tambahan = {}
status_login = False

def welcomePage():
    global status_login
    while True:
        print(f"{Fore.CYAN}\nUPS")
        print(Style.RESET_ALL)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print()
        pilihan_user = input("> ")
        if pilihan_user == "1":
            status_login = loginPage()
            if status_login:
                break
        elif pilihan_user == "2":
            registerPage()
        elif pilihan_user == "3":
            print(f"{Fore.CYAN}Terimakasih Telah Menggunakan UPS")
            print(Style.RESET_ALL)
            exit()
        else:
            print(f"{Fore.RED}Inputan tidak valid")
            print(Style.RESET_ALL)
            

def loginPage():
    while True:
        # username = input("Username: ")
        # password = input("Password: ")
        # if username in data_pengguna and data_pengguna[username] == password:
        #     print(f"{Fore.GREEN}Berhasil Login")
        #     print(Style.RESET_ALL)
        #     lanjutkan = input("Tekan Enter Untuk Melanjutkan")
        #     print()
        #     return True
        username = input("Username: ")
        password = input("Password: ")
        for user, password in data_pengguna.items():
            if user == username and password == password:
                print(f"{Fore.GREEN}Berhasil Login")
                print(Style.RESET_ALL)
                lanjutkan = input("Tekan Enter Untuk Melanjutkan")
                print()
                return True

            # if not berhasil_login:
            #     print(f"{Fore.RED}Gagal Login")
            #     print(Style.RESET_ALL)
        else:
            print(f"{Fore.RED}Login gagal")
            print(Style.RESET_ALL)
            while True:
                print("1. Login ulang")
                print("2. Register")
                print("3. Kembali ke welcome page")
                print()
                pilihan_user = input("> ")
                if pilihan_user == "1":
                    break
                elif pilihan_user == "2":
                    registerPage()
                    return False
                elif pilihan_user == "3":
                    return False
                else:
                    print(f"{Fore.RED}Inputan tidak valid")
                    print(Style.RESET_ALL)
                    

def registerPage():
    username = input("Username: ")
    while len(username) < 1:
        print("Username tidak boleh kosong")
        username = input("Username: ")
    password = input("Password: ")
    while len(password) < 8:
        print("Password harus memiliki minimal 8 karakter")
        password = input("Masukkan password: ")
    # nama = input("Nama: ")
    # kelamin = input("Jenis Kelamin: ")
    # alamat = input("Alamat: ")
    # nomor_hp = input("Nomor Hp: ")
    # riwayat_penyakit = input("Riwayat Penyakit (jika tidak ada - saja): ")
    print()
    data_pengguna[username] = password
    # data_tambahan = {
    #     'nama': nama,
    #     'kelamin': kelamin,
    #     'alamat': alamat,
    #     'nomor_hp': nomor_hp,
    #     'riwayat_penyakit': riwayat_penyakit
    # }
    print(f"{Fore.GREEN}Pengguna berhasil didaftarkan.")
    print(Style.RESET_ALL)

def menuObat():
    
    list_obat = [
        {"nama": "Bisolvon", "Jenis Obat": "Obat Batuk", "Kemasan": "Botol", "Isi": "60 ml" },
        {"nama": "Flutamol", "Jenis Obat": "Obat Flu", "Kemasan": "Botol", "Isi": "50 ml" },
        {"nama": "Sanmol", "Jenis Obat": "Obat Demam", "Kemasan": "Tablet", "Isi": "4 Tablet" },
        {"nama": "Paramex", "Jenis Obat": "Obat sakit Kepala", "Kemasan": "Tablet", "Isi": "8 Tablet" },
        {"nama": "Polysilane", "Jenis Obat": "Obat Magh", "Kemasan": "Botol", "Isi": "100 ml" },
        {"nama": "Aspirin", "Jenis Obat": "Obat Sakit Kepala", "Kemasan": "Tablet", "Isi": "8 Tablet" },
        {"nama": "Betadine", "Jenis Obat": "Obat Luka", "Kemasan": "Botol", "Isi": "30 ml" },
        {"nama": "Amoxicillin", "Jenis Obat": "Antibiotik", "Kemasan": "Tablet", "Isi": "12 Tablet" },
        {"nama": "Tretinoin", "Jenis Obat": "Obat Kulit", "Kemasan": "Tube", "Isi": "15 gram" },
    ]
    
    def informasiObat(pencarianObat):
        print(f"Nama Obat: {pencarianObat['nama']}")
        print(f"Jenis Obat: {pencarianObat['Jenis Obat']}")
        print(f"Kemasan: {pencarianObat['Kemasan']}")
        print(f"Isi: {pencarianObat['Isi']}")
        
        print()
        
        while True:
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print(f"{Fore.RED}Inputan tidak valid")
                print(f"{Fore.GREEN}Berhasil Login")
                

    def cariObat(nama):
        for i in list_obat:
            if i["nama"].lower() == nama.lower():
                return i
        return None

    while True:
        print("1. Bisolvon")
        print("2. Flutamol")
        print("3. Sanmol")
        print("4. Paramex")
        print("5. Polysilane")
        print("6. Aspirin")
        print("7. Betadine")
        print("8. Amoxicillin")
        print("9. Tretinoin")
        print("10. Kembali ke menu utama")
        print()
        print("11. Search")
        print()
        
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            hasil = cariObat("Bisolvon")
            
            informasiObat(hasil)
        elif pilihan_user == "2":
            hasil = cariObat("Flutamol")
            
            informasiObat(hasil)
        elif pilihan_user == "3":
            hasil = cariObat("Sanmol")
            
            informasiObat(hasil)
        elif pilihan_user == "4":
            hasil = cariObat("Paramex")
            
            informasiObat(hasil)
        elif pilihan_user == "5":
            hasil = cariObat("Polysillane")
            
            informasiObat(hasil)
        elif pilihan_user == "6":
            hasil = cariObat("Aspirin")
            
            informasiObat(hasil)
        elif pilihan_user == "7":
            hasil = cariObat("Betadine")
            
            informasiObat(hasil)
        elif pilihan_user == "8":
            hasil = cariObat("Amoxicillin")
            
            informasiObat(hasil)
        elif pilihan_user == "9":
            hasil = cariObat("Tretinoin")
            
            informasiObat(hasil)
        elif pilihan_user == "10":
            break
        elif pilihan_user == "11":
            while True:
                nama_obat = input("Masukkan nama barang yang ingin dicari: ")
                hasil = cariObat(nama_obat)
                
                if hasil != None:
                    informasiObat(hasil)
                else:
                    print("Obat tidak ditemukan")
        else:
            print(f"{Fore.RED}Inputan tidak valid")
            print(Style.RESET_ALL)
            
def menuKegiatan():
    def donorDarahPage():
        print(f"{Style.BRIGHT}\nDonor Darah: Sumbangkan Kebaikan, Sumbangkan Hidup")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Donor Darah kami! Di sini, kami membangun jembatan 
kebaikan antara kamu dan kesempatan untuk menyelamatkan nyawa. Donor darah 
adalah tindakan luar biasa yang memiliki dampak luar biasa pula.

Mengapa Donor Darah Penting?

Setiap detik, seseorang di luar sana membutuhkan bantuan darah 
untuk mempertahankan hidup. Dengan setiap donasi yang kamu berikan, 
kamu menjadi pahlawan bagi orang-orang yang sedang berjuang. 
Donor darah tidak hanya menyelamatkan nyawa, tetapi juga memberikan 
harapan bagi mereka yang memerlukan perawatan medis mendesak.

Bagaimana Proses Donor Darah?

Proses donor darah sederhana dan aman. Kami memiliki tim profesional 
yang siap membantu selama seluruh proses. Setelah pendaftaran dan pemeriksaan 
sederhana, kamu akan memberikan sumbangan darahmu. Satu tindakan kecil dari 
kamu bisa memiliki dampak besar dalam kehidupan orang lain.

Manfaat bagi Kesehatan

Selain membantu orang lain, donor darah juga memiliki manfaat bagi kesehatanmu 
sendiri. Ini adalah kesempatan untuk membersihkan dan meregenerasi sel-sel 
darahmu yang baru. Selain itu, proses ini dapat membantu mengurangi risiko 
penyakit tertentu dan meningkatkan kesehatan jantung.

Bergabunglah dalam Gerakan Kebaikan

Kami mengundangmu untuk bergabung dalam gerakan kebaikan ini. 
Informasi mengenai lokasi donor darah terdekat, jadwal acara, dan 
cara bergabung dengan komunitas kami dapat kamu temukan di sini.""")
        while True:
            print()
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print(f"{Fore.RED}Inputan tidak valid")
                print(Style.RESET_ALL)

    def vaksinasiPage():
        print(f"{Style.BRIGHT}\nVaksinasi: Langkah Proaktif untuk Kesehatan dan Perlindungan")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Vaksinasi kami! Di sini, kami menekankan pentingnya 
langkah proaktif dalam melindungi diri dan komunitas melalui vaksinasi.

Perlunya Vaksinasi

Vaksinasi adalah salah satu langkah terpenting dalam menjaga kesehatan kita. 
Ini bukan hanya tentang melindungi diri sendiri, tetapi juga tentang menjaga 
kesehatan orang-orang di sekitar kita. Vaksinasi membantu mencegah penyebaran 
penyakit dan mengurangi risiko komplikasi yang serius.

Manfaat Vaksinasi

Dapatkan informasi lengkap mengenai manfaat vaksinasi. Selain memberikan perlindungan 
diri dari penyakit tertentu, vaksinasi juga berperan dalam mengendalikan wabah penyakit, 
melindungi yang rentan, dan menciptakan kekebalan komunitas yang lebih luas.

Mitos dan Fakta

Dapatkan jawaban atas pertanyaan umum dan temukan fakta-fakta yang jelas mengenai 
vaksinasi. Kami hadir untuk memberikan informasi yang akurat dan terpercaya guna 
membantu menjawab keraguan atau pertanyaan yang mungkin kamu miliki tentang vaksinasi.

Bergabunglah dalam Perlindungan Bersama

Vaksinasi adalah langkah kecil dengan dampak besar. Mari bersama-sama menjadi bagian 
dari gerakan perlindungan dan kesehatan bersama. Dengan vaksinasi, kita membuka jalan 
menuju masa depan yang lebih sehat dan aman bagi kita semua.""")
        while True:
            print()
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print(f"{Fore.RED}Inputan tidak valid")
                print(Style.RESET_ALL)
    
    def senamBersamaPage():
        print(f"{Style.BRIGHT}\nSenam Bersama: Langkah Menuju Kesehatan dan Kebahagiaan")
        print()
        print(f"""{Style.RESET_ALL}
Selamat datang di halaman Senam Bersama kami! 
Di sini, kami mengajakmu untuk menemukan kebugaran, energi, 
dan keceriaan melalui sesi senam yang menyenangkan.

Mengapa Senam?

Senam bukan hanya tentang gerakan tubuh, tetapi juga tentang menjaga kesehatan dan kebugaran. 
Aktivitas fisik yang teratur membawa banyak manfaat bagi tubuh dan pikiran. Bersama-sama, 
kita bisa merasakan peningkatan energi, kekuatan, dan semangat yang positif.

Jenis Senam yang Ditawarkan

Temukan berbagai jenis senam yang ditawarkan di komunitas kami. Dari senam aerobik yang 
mengasyikkan hingga yoga yang menenangkan, ada sesi untuk setiap preferensi dan tingkat 
kebugaran. Jangan lewatkan kesempatan untuk merasakan beragam pengalaman senam yang bermanfaat.

Jadwal Sesi Senam

Cek jadwal lengkap dari sesi senam kami. Kami menyediakan waktu yang fleksibel untuk 
memastikan setiap orang dapat bergabung. Sesi-sesi ini tidak hanya tentang gerakan fisik, 
tetapi juga tentang menciptakan ikatan komunitas yang solid.

Manfaat Senam Teratur

Dapatkan informasi lengkap mengenai manfaat dari rutinitas senam secara teratur. Ini bukan 
hanya tentang kebugaran fisik, tetapi juga tentang kesehatan mental, peningkatan fokus, 
dan penurunan tingkat stres.

Bergabunglah dengan Komunitas Senam Kami

Ayo, jadikan setiap langkahmu sebagai langkah menuju kesehatan yang lebih baik bersama 
komunitas senam kami. Bergabunglah dengan kami dan rasakan kebahagiaan dalam setiap gerakan!
              """)
        while True:
            print()
            print("1. kembali ke menu sebelumnya")
            pilihan_user = input("> ")
            
            if pilihan_user == "1":
                break
            else:
                print(f"{Fore.RED}Inputan tidak valid")
                print(Style.RESET_ALL)
    
    list_kegiatan = [
        {"nama_kegiatan": "Donor Darah", 
         "deskripsi_kegiatan": """
    Kami hadir untuk mengajakmu menjadi bagian dari gerakan kebaikan melalui donor darah. 
    Dengan satu tindakan sederhana, kamu bisa menjadi pahlawan bagi mereka yang membutuhkan. 
    Di sini, temukan informasi lengkap tentang proses donor darah, manfaat bagi kesehatan, 
    serta jadwal lokasi dan waktu donor darah kami. Bergabunglah dengan komunitas kami untuk 
    emberikan harapan dan kehidupan kepada mereka yang membutuhkan. Jadilah bagian dari perubahan positif 
    dengan menyumbangkan satu tetes darah untuk kebaikan bersama.
         """},
        {"nama_kegiatan": "Vaksinasi",
         "deskripsi_kegiatan": """
    Jangan lewatkan kesempatan untuk melindungi diri dan orang-orang di sekitarmu! Halaman vaksinasi 
    kami adalah pintu menuju perlindungan dan keamanan. Temukan informasi tentang vaksin yang tersedia, 
    jadwal lokasi vaksinasi, dan pentingnya mendapatkan vaksin. Satu langkah kecil ini bisa menjadi langkah 
    besar untuk kesehatan dan keselamatan kita bersama. Ayo, bergabunglah dalam langkah proaktif melindungi 
    diri dari penyakit dengan vaksinasi.
         """},
        {"nama_kegiatan": "Senam Bersama",
         "deskripsi_kegiatan": """
    Rasakan energi, kebugaran, dan keceriaan dalam setiap gerakan! Halaman senam bersama kami adalah tempat 
    di mana kamu bisa bergabung dalam sesi senam yang menyenangkan dan bermanfaat. Dapatkan informasi tentang 
    jadwal, jenis senam yang ditawarkan, dan manfaat dari rutinitas senam secara teratur. Ayo, jadikan setiap 
    langkahmu sebagai langkah menuju kesehatan dan kebugaran yang lebih baik bersama komunitas senam kami!
         """}]
        

    for i, kegiatan in enumerate(list_kegiatan):
        print(f"""
{i+1}. Kegiatan {i+1}
   ---------------
    {kegiatan["nama_kegiatan"]}

    {kegiatan["deskripsi_kegiatan"]}
    """)
    
    while True:
        print("\nKegiatan UPS")
        print()
        print("1. Donor Darah")
        print("2. Vaksinasi")
        print("3. Senam Bersama")
        print("4. kembali ke menu sebelumnya")
        print()
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            donorDarahPage()
        elif pilihan_user == "2":
            vaksinasiPage()
        elif pilihan_user == "3":
            senamBersamaPage()
        elif pilihan_user == "4":
            break
        else:
            print(f"{Fore.RED}Inputan tidak valid")
            print(Style.RESET_ALL)
    
def menuUtama():
    global status_login
    while True:
        print("Selamat Datang Para Pasien")
        print()
        print("1. Obat")
        print("2. Kegiatan")
        print("3. Profile")
        print("4. Galeri")
        print("5. Tentang Kami")
        print("6. Logout")
        print()
        
        pilihan_user = input("> ")
        
        if pilihan_user == "1":
            menuObat()
        elif pilihan_user == "2":
            menuKegiatan()
        # elif pilihan_user == "3":
        #     menuProfile()
        # elif pilihan_user == "4":
        #     menuGaleri()
        # elif pilihan_user == "5":
        #     menuTentangKami()
        elif pilihan_user == "6":
            status_login = False
            return status_login
        else:
            print(f"{Fore.RED}Inputan tidak valid")
            print(Style.RESET_ALL)

        
while True:
    if not status_login:
        welcomePage()
    else:
        menuUtama()

# while True:
#     if not status_login:
#         welcomePage()
#     else:
#         print("Selamat datang")
#         print()
#         while True:
#             print("1. Logout")
#             print("2. Exit")
#             print()
#             pilihan_user = input("> ")
#             if pilihan_user == "1":
#                 status_login = False
#                 break
#             elif pilihan_user == "2":
#                 break
#             else:
#                 print("Inputan tidak valid")

class MesinAtm: #class mesin atm
    def __init__ (self):
        self.rekening = {
            "123456": {"Nama": "Darren", "Saldo": 1000000, "PIN": "213123"},
            "654321": {"Nama": "Lina", "Saldo": 500000, "PIN": "888999"},
            "987654": {"Nama": "Sariman", "Saldo": 750000, "PIN": "768932"},
        }
        self.percobaan = 0
        self.max_percobaan = 3 #untuk hitung percobaan login
        self.user_login= None
    def login(self): #sistem login atm
        while self.percobaan < self.max_percobaan: #jika percobaan login kurang dari 3 maka bisa login, kalo lebih dari 3 maka tidak bisa login
            no_rekening = input("Masukkan nomor rekening Anda: ").strip()
            if no_rekening in self.rekening:
                print(f"Selamat datang, {self.rekening[no_rekening]['Nama']}!")
                self.user_login = no_rekening
                self.pin()
                return
            else:
                print("Nomor rekening tidak valid. Silakan coba lagi.")
                self.percobaan += 1
            sisa = self.max_percobaan - self.percobaan
            print(f"Sisa percobaan: {sisa}")
        if self.percobaan == self.max_percobaan:
            print("Percobaan login telah habis. Silakan coba lagi nanti.")
            
    def pin(self): #sistem pin atm
        percobaan_pin = 0
        while percobaan_pin < self.max_percobaan:
            if self.user_login:
                pin = input("Masukkan PIN Anda: ").strip()
                if pin == self.rekening[self.user_login]["PIN"]:
                    print("PIN valid. Anda berhasil login.")
                    self.menu()
                    return
                else: #kalau masukin pin selama 3 kali gagal kartu di blokir
                    print("PIN tidak valid. Silakan coba lagi.") 
                    perintah = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
                    if perintah == "y":
                        percobaan_pin += 1
                    else:
                        print("Kartu anda untuk sementara di blokir. Silahkan bertanya kepada operator ATM untuk membantu anda.")
                        return
        if percobaan_pin == self.max_percobaan:
            print("Percobaan PIN telah habis. Silakan coba lagi nanti.")
            return

    def menu(self): #menu utama atm
        while True:
            print("\n=== Menu ATM ===") #opsi menu atm
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Setor Tunai")
            print("4. Keluar")
            pilihan = input("Pilih menu (1-4): ")
            if pilihan == "1":
                self.cek_saldo()
            elif pilihan == "2":
                self.tarik_tunai()
            elif pilihan == "3":
                self.setor_tunai()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan layanan ATM kami.")
                self.user_login = None
                break
    def cek_saldo(self): #cek  saldo atm
        if self.user_login:
            saldo = self.rekening[self.user_login]["Saldo"]
            print(f"Saldo Anda saat ini: Rp {saldo}")
        input("Tekan Enter untuk kembali ke menu utama...")
    def tarik_tunai(self):
        if self.user_login:
            saldo = self.rekening[self.user_login]["Saldo"]

            try:
                jumlah_tarik = int(input("Masukkan jumlah tarik tunai: "))
            except ValueError:
                print("Masukkan angka!")
                return

            if jumlah_tarik > saldo:
                print("Saldo tidak mencukupi.")
            else:
                self.rekening[self.user_login]["Saldo"] -= jumlah_tarik
                print(f"Berhasil menarik tunai sebesar Rp {jumlah_tarik}.")
                print(f"Saldo sekarang: Rp {self.rekening[self.user_login]['Saldo']}")

            input("Tekan Enter untuk kembali ke menu utama...")
    def setor_tunai(self): #setor tunai atm
        if self.user_login:
            try:
                jumlah_setor = int(input("Masukkan jumlah setor tunai: "))
            except ValueError:
                print("Masukkan angka!")
                return
            self.rekening[self.user_login]["Saldo"] += jumlah_setor
            print(f"Berhasil menyetor tunai sebesar Rp {jumlah_setor}.")
            print(f"Saldo Anda sekarang: Rp {self.rekening[self.user_login]['Saldo']}")
            input("Tekan Enter untuk kembali ke menu utama...")


atm = MesinAtm()
atm.login()
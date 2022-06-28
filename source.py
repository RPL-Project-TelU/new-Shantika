import csv
import getpass

 
def bookingbus():
    def kota():
        print("Pilih Kota Tujuan")
        print("Asal      \t Tujuan")
        print("- Bandung \t - Solo")
        print("- Bandung \t - Surabaya")
        print("- Bandung \t - Yogyakarta")
        print("- Bandung \t - Bali")
        print("")

    def tanggal():
        print("Tanggal Keberangkatan")
        
        global tanggal
        try:
            tanggal = int(input("Tanggal (1-31)       : "))
            while tanggal not in range (1,32):
                print ("\nMohon Masukkan Tanggal")
                tanggal = int(input("Tanggal (1-31)       : "))
        except ValueError:
            print("Mohon Masukkan Tanggal")
            tanggal = int(input("Tanggal (1-31)       : "))
        
        global bulan    
        try:
            bulan = int(input ("Bulan (1-12)         : "))
            while bulan not in range (1,13):
                print ("\Mohon Masukkan Bulan")
                bulan = int(input ("Bulan (1-12)         : "))
        except ValueError:
            print("Mohon Masukkan Bulan")
            bulan = int(input ("Bulan (1-12)         : "))    
        
        global tahun
        try:
            tahun = int(input ("Tahun                : "))
            while tahun < 2020:
                print ("Mohon Masukkan Tahun")
                tahun = int(input ("Tahun                : "))
        except ValueError:
            print ("Mohon Masukkan Tahun")
            tahun = int(input ("Tahun                : "))    
        
    def jumlahpenumpang():
        global penumpang_data
        try:
            penumpang_data = int(input("Jumlah Penumpang     : "))
        except ValueError:
            print("\Mohon Masukkan Jumlah Penumpang")
            jumlahpenumpang()
        
    def bandung_surabaya():
        bus = []
        with open('bandung_surabaya.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                bus.append(row)
        print("NO \t NAMABUS \t WAKTU \t\t HARGA")
        print("-" * 70)
        for data in bus:
            print(f"{data['NO']} \t {data['NAMABUS']} \t {data['WAKTU']} \t {data['HARGA']}")
            
    def bandung_solo():
        bus = []
        with open('bandung_solo.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                bus.append(row)
        print("NO \t NAMABUS \t WAKTU \t\t HARGA")
        print("-" * 70)
        for data in bus:
            print(f"{data['NO']} \t {data['NAMABUS']} \t {data['WAKTU']} \t {data['HARGA']}")

    def bandung_bali():
        bus = []
        with open('bandung_bali.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                bus.append(row)
        print("NO \t NAMABUS \t WAKTU \t\t HARGA")
        print("-" * 70)
        for data in bus:
            print(f"{data['NO']} \t {data['NAMABUS']} \t {data['WAKTU']} \t {data['HARGA']}")
            
    def bandung_yogyakarta():
        bus = []
        with open('bandung_yogyakarta.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                bus.append(row)
        print("NO \t NAMABUS \t WAKTU \t\t HARGA")
        print("-" * 70)
        for data in bus:
            print(f"{data['NO']} \t {data['NAMABUS']} \t {data['WAKTU']} \t {data['HARGA']}")
                

    def pesan():
        import math
        print("Booking Bus")
        juml_tiket = penumpang_data
        print("")

        global total_harga
        total_harga = juml_tiket * (int(bus[pilih]['Harga']))

     
    def totalHarga(): 
        print("Harga Tiket Yang Harus Dibayar           : Rp", total_harga)


                
    def nomorTelp():
        global nomor
        try:
            nomor = int(input("Nomor HP         : "))
        except ValueError:
            print ("Mohon Masukkan Nomor HP : ")
            nomorTelp()
           
    def data_pemesan():
        print("Data Pribadi")
        global pemesan
        pemesan =[]
        
        nama = input("Nama Lengkap     : ")
        while nama == "":
            print("\nMohon Masukkan Nama Lengkap")
            nama = input ("Nama Lengkap     : ")
            
        nomorTelp()
        
        email = input("Email            : ")
        while email == "":
            print ("Mohon Masukkan Email Anda")
            email = input ("Email            : ")
            
        pemesan.append(nama)
        pemesan.append(nomor)
        pemesan.append(email)
                  
    def penumpang():
        print("Data Pribadi")
        global datapenumpang
        datapenumpang =[]
        i = 1
        while i <= penumpang_data:
            dtpenumpang = {}
            print("Nama Penumpang ", i)
                  
            name  = input("Nama              : ")
            while name == "":
                print("Mohon Masukkan Nama Penumpang")
                name  = input("Nama              : ")              
                  
            dtpenumpang['Nama'] = name
            datapenumpang.append(dtpenumpang)
            i += 1
                
    def dataPenumpang():
        cIn = 0
        while cIn < penumpang_data:
            dt = datapenumpang[cIn]
            cIn += 1
            print(f" Penumpang {cIn}    : ", dt['Nama'])
                
                 
    def bus_detail():
        print("============  Tiket Booking Bus  ============")
        print("")
        print('Nama Bus         : ', bus[pilih]['NamaBus'])
        print('Tanggal          : ', "{}/{}/{}". format(tanggal, bulan, tahun))
        print('Lokasi Asal      : ', dari)
        print('Waktu Berangkat  : ', bus[pilih]['Waktu'][0:5])
        print('Lokasi Tujuan    : ', ke)
        print('Waktu Sampai     : ', bus[pilih]['Waktu'][8:13])
        print("")
        print("Data Pribadi")
        print("Nama Lengkap     : ", pemesan[0])
        print("Nomor HP         : ", pemesan[1])
        print("Email            : ", pemesan[2])
        print("\nData Penumpang")
        dataPenumpang()
        print("")
        totalHarga()
        print("")
        pembayaran()
        print("========== Bus Berhasil Di Booking ==========")

    def pembayaran():
        metode = int(input("Tuliskan Angka : "))
        print('''Pilih Metode Pembayaran
    1. Gopay
    2. Dana
    3. Ovo
    4. ATM
              ''')
        if metode == 1:
            print('''
    |--------------------|
    |                    |
    |                    |
    |                    |
    |        QR          |
    |                    |
    |                    |
    |                    |
    |--------------------|
    ''')

                  
    ulang = True
    inputuser = ""
    import os
    import time

    while ulang == True:
        print("\n==================================")
        print("       E - NEW SHANTHIKA          ")
        print("            Bandung          ")
        print("==================================")
        print("")
        
        kota()
                  
        dari = input("Asal          : ")
        while dari == "":
            print("Mohon Masukkan Daerah Asal")
            dari = input("Asal      :")
                  
        ke = input("Tujuan        : ")
        while ke == "":
            print("Mohon Masukkan Daerah Tujuan")
            dari = input("tujuan        : ")       
                  
        tanggal()
                  
        jumlahpenumpang()
        print("\n")
                  
        os.system("cls")
        

        if dari not in ['Bandung']:
            print("")
            print("Maaf, Bus Tidak Ada")
            continue
            
        elif ke not in ['Surabaya', 'Yogyakarta', 'Solo', 'Bali']:
            print("")
            print("maaf, Bus Tidak Ada")
            continue
        
        elif dari == "Bandung" and ke == "Surabaya":
            bandung_surabaya()
            f = open('bandung_surabaya.csv', 'r')
            reader = csv.reader(f)
            bus = {}
            for row in reader:
                bus[row[0]] = {'NamaBus':row[1],'Waktu':row[2],'Harga':row[3]}
            pilih = input("\nNomor bus : ")
            if pilih in bus:
                print("Nama Bus  : ", bus[pilih]['NamaBus'])
                print("Waktu     : ", bus[pilih]['Waktu'])
                print("Harga     :  RP.", bus[pilih]['Harga'])
            else:
                print("Bus Tidak Tersedia")
                continue
                
        elif dari == "Bandung" and ke == "Solo":
            bandung_solo()
            f = open('bandung_solo.csv', 'r')
            reader = csv.reader(f)
            bus = {}
            for row in reader:
                bus[row[0]] = {'NamaBus':row[1],'Waktu':row[2],'Harga':row[3]}
            pilih = input("\nNomor Bus : ")
            if pilih in bus:
                print("Nama Bus  : ", bus[pilih]['NamaBus'])
                print("Waktu     : ", bus[pilih]['Waktu'])
                print("Harga     :  RP.", bus[pilih]['Harga'])
            else:
                print("Bus Tidak tersedia")
                continue
        
        elif dari == "Bandung" and ke == "Bali":
            print("Daftar Harga Bus")
            bandung_bali()
            f = open('bandung_bali.csv', 'r')
            reader = csv.reader(f)
            bus = {}
            for row in reader:
                bus[row[0]] = {'NamaBus':row[1],'Waktu':row[2],'Harga':row[3]}
            pilih = input("\nNomor Bus : ")
            if pilih in bus:
                print("Nama Bus  : ", bus[pilih]['NamaBus'])
                print("Waktu     : ", bus[pilih]['Waktu'])
                print("Harga     :  RP.", bus[pilih]['Harga'])
            else:
                print("Bus Tidak tersedia")
                continue
                
        elif dari == "Bandung" and ke == "Yogyakarta":
            bandung_yogyakarta()
            f = open('bandung_yogyakarta.csv', 'r')
            reader = csv.reader(f)
            bus = {}
            for row in reader:
                bus[row[0]] = {'NamaBus':row[1],'Waktu':row[2],'Harga':row[3]}
            pilih = input("\nNomor Bus : ")
            if pilih in bus:
                print("Nama Bus  : ", bus[pilih]['NamaBus'])
                print("Waktu     : ", bus[pilih]['Waktu'])
                print("harga     :  RP.", bus[pilih]['Harga'])
            else:
                print("Bus Tidak tersedia")
                continue
              
                  
        print("")
        pesan()
        print("")
        data_pemesan()
        print("")
        penumpang()
        print("")
        os.system("cls")
        bus_detail()
        print("")


        inputuser = input("Ingin Melakukan Transaksi Lain? (ya/tidak) : ")
        if inputuser != "ya":
            ulang = False
            
    print("")
    print ("Terima Kasih")
    dashboard()

    

katasandi = []                          

print('-----------------------------------------')

print('           Daftarkan Akun Anda                ')

print('-----------------------------------------')

daftar_email = input("Masukkan Email : ") 

daftar_sandi = getpass.getpass('Masukkan Sandi : ')

 

def konfirmasi():

    konfirm = getpass.getpass('Konfirmasi Ulang : ')

    katasandi.append(konfirm)    

    if konfirm == daftar_sandi:

        print('Sandi Cocok')    

    else:

        print('Sandi Tidak Sesuai')

        konfirmasi()       

konfirmasi()

 

print('-----------------------------------------')

print('                  Login                  ')

print('-----------------------------------------')

def konfirmasi1():

    email1 = input('Masukkan Email : ')

    if email1 == daftar_email:

        pass

    else:

        print('Email Tidak Terdaftar')

        konfirmasi1()

        

konfirmasi1() 

sandi = getpass.getpass('Masukkan Sandi : ')

if sandi == daftar_sandi:

    print('Anda Telah Login')
    bookingbus()
    

else:

    print('Kata Sandi salah')

print('------------------------------------------')




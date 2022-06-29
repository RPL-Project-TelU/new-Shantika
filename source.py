import csv
import getpass
from enum import Enum
import os
import time
 
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
        
        global tgl
        try:
            tgl = int(input("Tanggal (1-31)       : "))
            while tgl not in range (1,32):
                print ("\nMohon Masukkan Tanggal")
                tgl = int(input("Tanggal (1-31)       : "))
        except ValueError:
            print("Mohon Masukkan Tanggal")
            tgl = int(input("Tanggal (1-31)       : "))
        
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
        print('Tanggal          : ', "{}/{}/{}". format(tgl, bulan, tahun))
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
        

    def pembayaran():
        
        print('''Pilih Bank Yang Anda inginkan untuk pembayaran
    1. BNI
    2. BRI
    3. Mandiri
    4. BCA
              ''')
        metode = str(input("Tuliskan Nama Bank (BNI, BRI, Mandiri, BCA): "))
        if metode == "BNI":
            print("Nama Bank", metode)
            print("Nomor Rekening Pembayaran")
            print("\n")
            print("123", nomor)
        elif metode == "BRI":
            print("Nama Bank", metode)
            print("Nomor Rekening Pembayaran")
            print("\n")
            print("456", nomor)
        elif metode == "Mandiri":
            print("Nama Bank", metode)
            print("Nomor Rekening Pembayaran")
            print("\n")
            print("789", nomor)
        elif metode == "BCA":
            print("Nama Bank", metode)
            print("Nomor Rekening Pembayaran")
            print("\n")
            print("100", nomor)
        else:
            print("Bank Anda tidak terdaftar")
        print("\n")    
        print("Ketik 'KONFIRMASI', jika anda telah melakukan pembayaran")
        
        konfirmasi = str(input("Konfirmasi pembayaran = "))
        if (konfirmasi == "KONFIRMASI"):
            print("\n")
            print("========== Bus Berhasil Di Pesan ==========")           

    ProgramUtama = True
    inputuser = ""        
    while ProgramUtama == True:
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
        inputuser = input("Ingin Melakukan Transaksi Lagi (ya/tidak)? ")
        if inputuser != "ya":
            ProgramUtama = False
            
    print("")
    print ("Terima Kasih")
    
    
#automata
#1302204034
class TiketBusStatus(Enum):
    LogIn = 0
    Dashboard = 1
    Tambahkan_Bus = 2
    Cari_Bus = 3

class Trigger(Enum):
    Gagal_Login = 0
    Pesan_Tiket = 1
    Menambahkan_Tiket = 2
    Mencari_Tiket = 3

class transition():
    prevState : TiketBusStatus
    nextState : TiketBusStatus
    trigger : Trigger

    def __init__(self,prevState:TiketBusStatus, nextState:TiketBusStatus, trigger:Trigger):
        self.prevState = prevState
        self.nextState = nextState
        self.trigger = trigger

p : transition = [transition(TiketBusStatus.LogIn, TiketBusStatus.Dashboard, Trigger.Pesan_Tiket),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.Tambahkan_Bus, Trigger.Menambahkan_Tiket),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.Cari_Bus, Trigger.Mencari_Tiket),
                    transition(TiketBusStatus.LogIn, TiketBusStatus.LogIn, Trigger.Gagal_Login),
                ]

currentState : TiketBusStatus = "LogIn"
def getNextState(prevState:TiketBusStatus, trigger:Trigger):
    nextState : TiketBusStatus = prevState
    i = 0
    for i in range(len(p)):
        if p[i].prevState.name == prevState and p[i].trigger.name == trigger:
            nextState = p[i].nextState
    return nextState

def activeTrigger(trigger:Trigger):
    global currentState
    nextState:TiketBusStatus = getNextState(currentState, Trigger[trigger].name)
    currentState = nextState

katasandi = []                          
#halaman register akun
print('-----------------------------------------')
print('           Daftarkan Akun Anda                ')
print('-----------------------------------------')
#input email dan kata sandi
daftar_email = input("Email : ") 
daftar_sandi = getpass.getpass('Kata Sandi : ')
#konfirmasi kata sandi
def konfirmasi():
    konfirm = getpass.getpass('Konfirmasi Ulang : ')
    katasandi.append(konfirm)    
    #kata sandi sesuai
    if konfirm == daftar_sandi:
        print("Kata Sandi Sesuai")
        print("Halaman",currentState)    
    #kata sandi tidak sesuai
    else:
        print('Kata Sandi Tidak Sesuai')
        konfirmasi()       
konfirmasi()
#halaman login
print('-----------------------------------------')
print('                  Login                  ')
print('-----------------------------------------')
#email
def konfirmasi1():
    #input email
    email1 = input('Email : ')
    #email terdaftar
    if email1 == daftar_email:
        pass
    #email tidak terdaftar
    else:
        print('Email Tidak Terdaftar')
        konfirmasi1()
konfirmasi1() 
#kata sandi
sandi = getpass.getpass('Kata Sandi : ')

if sandi == daftar_sandi:
    print('Login Berhasil')
    print("Program Pemasanan Tiket Bus Shantika")
    y =  input("Ketik (Pesan_Tiket) untuk pesan tiket bus: ")
    activeTrigger(y)
    print("Halaman",currentState.name)
    bookingbus()
    
else:
    print('Kata Sandi Salah')
print('------------------------------------------')